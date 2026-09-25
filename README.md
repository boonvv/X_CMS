# X_CMS

A full-stack workspace, project, task, and content management platform.

## Stack
- **API:** FastAPI, Strawberry GraphQL, SQLAlchemy, SQLite, JWT
- **Web:** Vite, React, TypeScript, responsive dark-sidebar UI

## Run locally

```bash
# API
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload

# Web (another terminal)
cd frontend
npm install
npm run dev
```

The API is available at `http://localhost:8000/graphql` and interactive docs at `/docs`.
