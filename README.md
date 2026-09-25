* {
  box-sizing: border-box;
}

html, body, #root {
  margin: 0;
  min-height: 100%;
  height: 100%;
  background: #0d1117;
  color: #e8ecf4;
  font-family: 'Inter', 'Segoe UI', sans-serif;
}

body {
  min-height: 100vh;
}

a {
  color: inherit;
  text-decoration: none;
}

button, input, textarea {
  font: inherit;
}

button {
  cursor: pointer;
}

.auth-page {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 22px;
  background: radial-gradient(circle at top, #171d31 0%, #090d14 45%, #06080d 100%);
}

.auth-card {
  width: min(440px, 100%);
  padding: 32px 28px;
  border: 1px solid rgba(255,255,255,0.07);
  background: rgba(18, 22, 29, 0.9);
  border-radius: 18px;
  box-shadow: 0 20px 50px rgba(0,0,0,0.32);
}

.brand-line {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.04em;
  margin-bottom: 20px;
}

.brand-mark {
  display: inline-flex;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #7c6af6, #58b7f9);
  color: white;
  font-size: 1rem;
}

.auth-card h1 {
  margin: 0;
  font-size: clamp(2rem, 4vw, 2.4rem);
  letter-spacing: -0.05em;
}

.muted {
  color: #9aa7ba;
}

.auth-form {
  display: grid;
  gap: 14px;
  margin-top: 24px;
}

.auth-form input {
  width: 100%;
  border-radius: 11px;
  border: 1px solid rgba(168, 181, 205, 0.2);
  background: rgba(255,255,255,0.02);
  color: #f4f8ff;
  padding: 14px 16px;
  outline: none;
}

.primary-button, .ghost-button, .upload-button, .logout-button, .nav-item, .icon-button, .checkbox, .download-link {
  transition: 0.2s ease;
}

.primary-button {
  border: none;
  background: linear-gradient(135deg, #765af7, #4ca5ff);
  color: white;
  font-weight: 600;
  border-radius: 12px;
  padding: 13px 16px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.primary-button.small {
  padding: 10px 12px;
  border-radius: 10px;
}

.primary-button:hover {
  filter: brightness(1.05);
}

.text-button {
  display: block;
  width: 100%;
  margin-top: 18px;
  background: transparent;
  border: none;
  color: #9dd0ff;
  font-weight: 600;
}

.error-box {
  padding: 10px 12px;
  border-radius: 10px;
  background: rgba(255, 82, 82, 0.1);
  border: 1px solid rgba(255, 82, 82, 0.24);
  color: #ffb2b2;
}

.app-shell {
  min-height: 100vh;
  display: flex;
  background: #0b1017;
}

.sidebar {
  width: 250px;
  background: rgba(17, 21, 28, 0.96);
  border-right: 1px solid rgba(255,255,255,0.06);
  padding: 28px 18px 20px;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.brand-line {
  display: flex;
  align-items: center;
  gap: 10px;
  letter-spacing: -0.04em;
}

.sidebar-nav {
  display: grid;
  gap: 8px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 12px;
  border-radius: 12px;
  color: #b4bfd1;
  text-decoration: none;
}

.nav-item.active,
.nav-item:hover {
  background: rgba(255,255,255,0.04);
  color: white;
}

.logout-button {
  margin-top: auto;
  background: rgba(255,255,255,0.02);
  color: #dfe8ff;
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 12px;
  padding: 12px 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.main-panel {
  flex: 1;
  padding: 38px 32px 48px;
  background: #0d1118;
}

.page-header, .section-row, .topbar-row, .panel-header, .project-card-header, .modal-actions, .content-card-header, .editor-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.page-header {
  margin-bottom: 26px;
}

.page-header h1 {
  margin: 10px 0 0;
  font-size: clamp(2.1rem, 3vw, 2.9rem);
  letter-spacing: -0.05em;
}

.eyebrow {
  color: #7f8ea7;
  letter-spacing: 0.12em;
  font-size: 0.68rem;
  text-transform: uppercase;
}

.search-box {
  min-width: 260px;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 11px 14px;
  border-radius: 12px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
  color: #aab6cc;
}

.search-box input {
  background: transparent;
  border: none;
  outline: none;
  color: white;
  width: 100%;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(180px, 1fr));
  gap: 14px;
  margin-bottom: 28px;
}

.stat-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 16px;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 18px 16px;
}

.stat-icon {
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, rgba(118,90,247,0.2), rgba(76,165,255,0.2));
  border-radius: 12px;
  color: #afc9ff;
}

.stat-label {
  font-size: 0.72rem;
  color: #8b97ad;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.stat-value {
  font-weight: 700;
  font-size: 2rem;
  letter-spacing: -0.05em;
}

.section-row {
  margin: 16px 0 18px;
}

.section-row h2,
.panel-box h3,
.summary-card h3,
.media-panel h3 {
  margin: 0;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 18px;
}

.project-card,
.new-project-card,
.panel-box,
.summary-card,
.content-card,
.page-card {
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px;
  padding: 18px;
}

.project-card {
  cursor: pointer;
}

.project-card:hover {
  transform: translateY(-2px);
  border-color: rgba(124, 106, 246, 0.4);
}

.project-color {
  width: 11px;
  height: 11px;
  border-radius: 10px;
}

.tiny-label {
  font-size: 0.7rem;
  color: #7f8ea7;
  letter-spacing: 0.11em;
}

.project-card h3 {
  margin: 14px 0 8px;
  font-size: 1.4rem;
  letter-spacing: -0.04em;
}

.small {
  font-size: 0.9rem;
}

.mini-progress {
  margin-top: 18px;
  display: grid;
  gap: 8px;
}

.meta-row {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  color: #a5b1c3;
  font-size: 0.82rem;
}

.progress-track {
  width: 100%;
  height: 8px;
  border-radius: 999px;
  background: rgba(255,255,255,0.08);
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  border-radius: inherit;
}

.new-project-card {
  min-height: 220px;
  display: grid;
  place-items: center;
  text-align: center;
  color: #d7e7ff;
  font-weight: 600;
  background: rgba(255,255,255,0.02);
}

.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(5, 7, 12, 0.7);
  display: grid;
  place-items: center;
  z-index: 100;
  padding: 18px;
}

.modal-panel,
.editor-modal {
  width: min(480px, 100%);
  background: #101821;
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px;
  padding: 22px;
}

.modal-panel h2 {
  margin: 0 0 18px;
}

.modal-panel input,
.modal-panel textarea,
.task-input-row input,
.editor-modal textarea {
  width: 100%;
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(255,255,255,0.02);
  border-radius: 12px;
  padding: 12px 14px;
  color: white;
  margin-bottom: 14px;
  outline: none;
}

.modal-panel textarea,
.editor-modal textarea {
  resize: vertical;
  min-height: 120px;
}

.color-picker-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 14px;
}

.color-picker-row input[type="color"] {
  width: 48px;
  height: 38px;
  padding: 4px;
  border-radius: 10px;
}

.ghost-button {
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(255,255,255,0.025);
  color: #eaf1ff;
  border-radius: 10px;
  padding: 11px 12px;
}

.ghost-button.small {
  padding: 8px 10px;
  font-size: 0.82rem;
}

.upload-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: rgba(118, 90, 247, 0.12);
  border: 1px solid rgba(118,90,247,0.45);
  border-radius: 12px;
  padding: 11px 13px;
  color: #efebff;
  cursor: pointer;
}

.upload-button input {
  display: none;
}

.project-header {
  margin: 12px 0 18px;
}

.project-summary {
  display: grid;
  grid-template-columns: repeat(2, minmax(220px, 1fr));
  gap: 18px;
  margin-bottom: 18px;
}

.summary-card {
  min-height: 120px;
}

.metric-row {
  display: flex;
  align-items: end;
  gap: 8px;
  margin: 16px 0;
}

.metric-row strong {
  font-size: 2rem;
  letter-spacing: -0.05em;
}

.summary-card p {
  color: #b3bed3;
  margin: 18px 0 0;
}

.split-columns {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 18px;
  margin-top: 16px;
}

.panel-header {
  margin-bottom: 16px;
}

.panel-header span {
  color: #8190ac;
}

.task-input-row {
  display: flex;
  gap: 10px;
  margin-bottom: 14px;
}

.task-input-row input {
  flex: 1;
  margin-bottom: 0;
}

.task-list,
.file-list {
  display: grid;
  gap: 10px;
}

.task-item,
.file-item {
  display: flex;
  align-items: center;
  gap: 12px;
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 12px;
  background: rgba(255,255,255,0.02);
  padding: 10px 12px;
}

.checkbox {
  width: 26px;
  height: 26px;
  border-radius: 8px;
  display: grid;
  place-items: center;
  border: 1px solid rgba(255,255,255,0.12);
  background: transparent;
  color: #ccd6e8;
}

.checkbox.checked {
  background: rgba(46, 196, 121, 0.12);
  border-color: rgba(46, 196, 121, 0.3);
  color: #52d58c;
}

.task-text {
  flex: 1;
  color: #edf4ff;
}

.task-text.done {
  text-decoration: line-through;
  color: #7d8ea8;
}

.icon-button {
  background: transparent;
  border: none;
  color: #bbcadf;
}

.file-meta {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  min-width: 0;
}

.file-meta span {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.file-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.download-link {
  color: #c0daff;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.media-panel {
  margin-top: 22px;
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px;
  padding: 18px;
}

.media-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 18px;
  margin-top: 18px;
}

.media-card {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  overflow: hidden;
}

.media-card img,
.media-card video,
.content-card img,
.content-card video {
  display: block;
  width: 100%;
  max-height: 220px;
  object-fit: cover;
  background: #0a111b;
}

.media-card div {
  padding: 10px 12px;
  color: #dfeaff;
}

.editor-modal {
  width: min(760px, 100%);
}

.editor-header {
  margin-bottom: 16px;
}

.editor-modal textarea {
  min-height: 340px;
  margin-bottom: 0;
}

.content-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 18px;
}

.content-card {
  display: grid;
  gap: 12px;
}

.content-card-header {
  color: #a9b6ce;
}

.content-name {
  color: #eff5ff;
  font-weight: 600;
  word-break: break-word;
}

.content-placeholder {
  min-height: 110px;
  display: grid;
  place-items: center;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 12px;
  color: #a9b6ce;
}

.content-actions {
  display: flex;
  justify-content: flex-end;
}

.admin-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(240px, 1fr));
  gap: 18px;
}

.info-stack {
  display: grid;
  gap: 12px;
  margin-top: 18px;
}

.info-stack div {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  padding: 12px 14px;
  border-radius: 12px;
  background: rgba(255,255,255,0.02);
  color: #dce6f9;
}

.info-stack strong {
  color: #9daec9;
}

.empty-state {
  color: #9aa7ba;
  padding: 18px 0;
}

@media (max-width: 960px) {
  .app-shell {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid rgba(255,255,255,0.06);
  }

  .stats-grid,
  .project-summary,
  .split-columns,
  .admin-grid {
    grid-template-columns: 1fr;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .search-box {
    width: 100%;
  }
}

@media (max-width: 620px) {
  .main-panel {
    padding: 24px 18px 40px;
  }

  .sidebar {
    padding: 22px 14px 16px;
  }

  .project-grid {
    grid-template-columns: 1fr;
  }
}
