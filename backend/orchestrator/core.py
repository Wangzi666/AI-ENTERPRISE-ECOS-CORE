from backend.evolution.engine import evolve
from backend.factory.agent_factory import create_agent

def run_cycle():
    evolve("system_check")
    create_agent("auto_seo", ["seo", "analysis"])
    return {"status": "cycle complete", "autonomy": "enabled"}
