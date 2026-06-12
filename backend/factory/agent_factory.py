AGENT_BLUEPRINTS = {}

def create_agent(name, skills):
    AGENT_BLUEPRINTS[name] = {
        "skills": skills,
        "status": "active",
        "autonomy": 0.7
    }
    return AGENT_BLUEPRINTS[name]

def list_agents():
    return AGENT_BLUEPRINTS
