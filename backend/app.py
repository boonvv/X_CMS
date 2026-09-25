import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import strawberry
from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, sessionmaker
from strawberry.fastapi import GraphQLRouter

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./x_cms.db")
UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "./uploads")); UPLOAD_DIR.mkdir(exist_ok=True)
SECRET = os.getenv("JWT_SECRET", "change-this-secret-in-production")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False)
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)

class Base(DeclarativeBase): pass
class User(Base):
    __tablename__="users"; id: Mapped[int]=mapped_column(primary_key=True); email: Mapped[str]=mapped_column(String(255), unique=True); name: Mapped[str]=mapped_column(String(120)); password: Mapped[str]=mapped_column(String(255)); is_admin: Mapped[bool]=mapped_column(Boolean, default=False)
    projects: Mapped[list["Project"]]=relationship(back_populates="owner", cascade="all, delete-orphan")
class Project(Base):
    __tablename__="projects"; id: Mapped[int]=mapped_column(primary_key=True); name: Mapped[str]=mapped_column(String(160)); description: Mapped[str]=mapped_column(Text, default=""); color: Mapped[str]=mapped_column(String(20), default="#7c5cff"); owner_id: Mapped[int]=mapped_column(ForeignKey("users.id")); created_at: Mapped[datetime]=mapped_column(DateTime, default=datetime.utcnow)
    owner: Mapped[User]=relationship(back_populates="projects"); tasks: Mapped[list["Task"]]=relationship(cascade="all, delete-orphan"); files: Mapped[list["ContentFile"]]=relationship(cascade="all, delete-orphan")
class Task(Base):
    __tablename__="tasks"; id: Mapped[int]=mapped_column(primary_key=True); title: Mapped[str]=mapped_column(String(240)); completed: Mapped[bool]=mapped_column(Boolean, default=False); project_id: Mapped[int]=mapped_column(ForeignKey("projects.id"))
class ContentFile(Base):
    __tablename__="content_files"; id: Mapped[int]=mapped_column(primary_key=True); name: Mapped[str]=mapped_column(String(255)); path: Mapped[str]=mapped_column(String(500)); mime: Mapped[str]=mapped_column(String(120), default="application/octet-stream"); project_id: Mapped[int]=mapped_column(ForeignKey("projects.id")); uploaded_at: Mapped[datetime]=mapped_column(DateTime, default=datetime.utcnow)
Base.metadata.create_all(engine)

def token(user_id: int): return jwt.encode({"sub": str(user_id), "exp": datetime.utcnow()+timedelta(days=7)}, SECRET, algorithm="HS256")
def current_user(info) -> User:
    auth = info.context.get("authorization", "")
    if not auth.startswith("Bearer "): raise Exception("Authentication required")
    try: uid = int(jwt.decode(auth[7:], SECRET, algorithms=["HS256"])["sub"])
    except (JWTError, KeyError, ValueError): raise Exception("Invalid or expired token")
    with SessionLocal() as db: user = db.get(User, uid); 
    if not user: raise Exception("User not found")
    return user

def project_dict(p, db):
    tasks = db.query(Task).filter_by(project_id=p.id).all(); files=db.query(ContentFile).filter_by(project_id=p.id).all()
    return ProjectType(id=p.id,name=p.name,description=p.description,color=p.color,created_at=p.created_at.isoformat(),tasks=[TaskType(id=t.id,title=t.title,completed=t.completed) for t in tasks],files=[FileType(id=f.id,name=f.name,mime=f.mime) for f in files])

@strawberry.type
class TaskType: id:int; title:str; completed:bool
@strawberry.type
class FileType: id:int; name:str; mime:str
@strawberry.type
class ProjectType: id:int; name:str; description:str; color:str; created_at:str; tasks:list[TaskType]; files:list[FileType]
@strawberry.type
class AuthType: token:str; user_id:int; name:str; email:str
@strawberry.type
class StatsType: projects:int; tasks:int; completed:int; files:int

@strawberry.type
class Query:
    @strawberry.field
    def me(self, info) -> AuthType:
        u=current_user(info); return AuthType(token="",user_id=u.id,name=u.name,email=u.email)
    @strawberry.field
    def projects(self, info) -> list[ProjectType]:
        u=current_user(info)
        with SessionLocal() as db: return [project_dict(p,db) for p in db.query(Project).filter_by(owner_id=u.id).order_by(Project.created_at.desc()).all()]
    @strawberry.field
    def stats(self, info) -> StatsType:
        u=current_user(info)
        with SessionLocal() as db:
            ps=db.query(Project).filter_by(owner_id=u.id).all(); ids=[p.id for p in ps]; ts=db.query(Task).filter(Task.project_id.in_(ids)).all() if ids else []
            return StatsType(projects=len(ps),tasks=len(ts),completed=sum(t.completed for t in ts),files=db.query(ContentFile).filter(ContentFile.project_id.in_(ids)).count() if ids else 0)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def signup(self, name:str, email:str, password:str) -> AuthType:
        with SessionLocal() as db:
            if db.query(User).filter_by(email=email.lower()).first(): raise Exception("Email already registered")
            u=User(name=name,email=email.lower(),password=pwd.hash(password)); db.add(u); db.commit(); db.refresh(u); return AuthType(token=token(u.id),user_id=u.id,name=u.name,email=u.email)
    @strawberry.mutation
    def login(self, email:str, password:str) -> AuthType:
        with SessionLocal() as db:
            u=db.query(User).filter_by(email=email.lower()).first()
            if not u or not pwd.verify(password,u.password): raise Exception("Invalid email or password")
            return AuthType(token=token(u.id),user_id=u.id,name=u.name,email=u.email)
    @strawberry.mutation
    def create_project(self, info, name:str, description:str="", color:str="#7c5cff") -> ProjectType:
        u=current_user(info)
        with SessionLocal() as db: p=Project(name=name,description=description,color=color,owner_id=u.id); db.add(p); db.commit(); db.refresh(p); return project_dict(p,db)
    @strawberry.mutation
    def delete_project(self, info, project_id:int) -> bool:
        u=current_user(info)
        with SessionLocal() as db:
            p=db.query(Project).filter_by(id=project_id,owner_id=u.id).first()
            if not p: raise Exception("Project not found")
            db.delete(p); db.commit(); return True
    @strawberry.mutation
    def create_task(self, info, project_id:int, title:str) -> TaskType:
        u=current_user(info)
        with SessionLocal() as db:
            if not db.query(Project).filter_by(id=project_id,owner_id=u.id).first(): raise Exception("Project not found")
            t=Task(project_id=project_id,title=title); db.add(t); db.commit(); db.refresh(t); return TaskType(id=t.id,title=t.title,completed=t.completed)
    @strawberry.mutation
    def toggle_task(self, info, task_id:int) -> TaskType:
        u=current_user(info)
        with SessionLocal() as db:
            t=db.get(Task,task_id); p=db.get(Project,t.project_id) if t else None
            if not t or not p or p.owner_id != u.id: raise Exception("Task not found")
            t.completed=not t.completed; db.commit(); return TaskType(id=t.id,title=t.title,completed=t.completed)
    @strawberry.mutation
    def delete_task(self, info, task_id:int) -> bool:
        u=current_user(info)
        with SessionLocal() as db:
            t=db.get(Task,task_id); p=db.get(Project,t.project_id) if t else None
            if not t or not p or p.owner_id != u.id: raise Exception("Task not found")
            db.delete(t); db.commit(); return True

schema=strawberry.Schema(query=Query, mutation=Mutation)
app=FastAPI(title="X_CMS API")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
def gql_context(request): return {"authorization":request.headers.get("authorization","")}
app.include_router(GraphQLRouter(schema,context_getter=gql_context),prefix="/graphql")

@app.post("/projects/{project_id}/files")
async def upload_file(project_id:int, file:UploadFile=File(...), authorization:Optional[str]=None):
    # Browser clients pass the bearer token in the Authorization header; FastAPI exposes it below.
    with SessionLocal() as db:
        try: uid=int(jwt.decode(authorization or "",SECRET,algorithms=["HS256"])["sub"])
        except Exception: raise HTTPException(401,"Authentication required")
        if not db.query(Project).filter_by(id=project_id,owner_id=uid).first(): raise HTTPException(404,"Project not found")
        safe=Path(file.filename or "upload.bin").name; target=UPLOAD_DIR/f"{uid}_{project_id}_{safe}"; target.write_bytes(await file.read())
        item=ContentFile(name=safe,path=str(target),mime=file.content_type or "application/octet-stream",project_id=project_id); db.add(item); db.commit(); db.refresh(item); return {"id":item.id,"name":item.name}
@app.get("/files/{file_id}")
def download_file(file_id:int):
    with SessionLocal() as db: f=db.get(ContentFile,file_id)
    if not f or not Path(f.path).exists(): raise HTTPException(404,"File not found")
    return FileResponse(f.path,media_type=f.mime,filename=f.name)
