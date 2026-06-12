CORPORATIONS = {}

def create_corporation(name):
    CORPORATIONS[name] = {
        "ceo": "AI",
        "revenue": 0,
        "agents": []
    }
    return CORPORATIONS[name]

def run_corporation(name):
    corp = CORPORATIONS.get(name, {})
    corp["revenue"] += 1000
    return corp
