Write-Host "🚀 AI ENTERPRISE OS SPRINT 1 BOOTSTRAP START" -ForegroundColor Green

$root = Get-Location

# =========================
# STRUCTURE
# =========================
$dirs = @(
 "backend/core/identity",
 "backend/core/registry",
 "backend/core/agents",
 "backend/api",
 "backend/services",
 "frontend",
 "infra",
 "docs"
)

foreach ($d in $dirs) {
 New-Item -ItemType Directory -Force -Path "$root\$d" | Out-Null
}

# =========================
# BACKEND CORE
# =========================
@"
from fastapi import FastAPI

app = FastAPI(title="AI Enterprise OS - Sprint 1")

USERS = {}
COMPANIES = {}
AGENTS = {}

@app.post("/identity/user")
def create_user(user: dict):
    USERS[user["id"]] = user
    return {"status": "created", "user": user}

@app.post("/identity/company")
def create_company(company: dict):
    COMPANIES[company["id"]] = company
    return {"status": "created", "company": company}

@app.post("/agents/bind")
def bind_agent(payload: dict):
    AGENTS[payload["agent_id"]] = payload
    return {"status": "bound", "data": payload}

@app.get("/system")
def system():
    return {
        "status": "AI ENTERPRISE OS SPRINT 1 ACTIVE",
        "users": len(USERS),
        "companies": len(COMPANIES),
        "agents": len(AGENTS)
    }
"@ | Out-File "$root\backend\main.py" -Encoding utf8

# =========================
# DOCKER
# =========================
@"
version: '3.9'

services:
  backend:
    build: ./backend
    ports:
      - '8000:8000'
"@ | Out-File "$root\docker-compose.yml" -Encoding utf8

# =========================
# DOCKERFILE
# =========================
@"
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn
CMD ["uvicorn","backend.main:app","--host","0.0.0.0","--port","8000"]
"@ | Out-File "$root\backend\Dockerfile" -Encoding utf8

# =========================
# GIT PUSH
# =========================
git add .
git commit -m "Sprint 1 Identity & Registry bootstrap"
git branch -M main
git push -u origin main

Write-Host "✅ SPRINT 1 COMPLETE + PUSHED TO GITHUB" -ForegroundColor Green
