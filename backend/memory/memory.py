MEMORY = []

def store_memory(agent, data):
    MEMORY.append({
        "agent": agent,
        "data": data
    })
    return {"status": "stored"}
