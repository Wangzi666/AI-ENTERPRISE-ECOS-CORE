CONNECTORS = {
    "ozon": {"status": "connected"},
    "wb": {"status": "connected"},
    "yandex": {"status": "connected"}
}

def sync_platform(name):
    return {"platform": name, "sync": "completed"}
