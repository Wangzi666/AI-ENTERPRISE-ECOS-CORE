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
