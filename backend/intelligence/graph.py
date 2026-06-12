GLOBAL_GRAPH = {
    "companies": {},
    "agents": {},
    "transactions": [],
    "risk": {}
}

def ingest(entity_type, data):
    if entity_type not in GLOBAL_GRAPH:
        GLOBAL_GRAPH[entity_type] = {}
    GLOBAL_GRAPH[entity_type].update(data)
    return GLOBAL_GRAPH
