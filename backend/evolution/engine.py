EVOLUTION_LOG = []

def evolve(system_event):
    update = {
        "event": system_event,
        "action": "system optimized",
        "score": 0.92
    }
    EVOLUTION_LOG.append(update)
    return update

def get_evolution():
    return EVOLUTION_LOG
