PLUGINS = {
    "ozon_connector": {"status": "active"},
    "wb_connector": {"status": "active"},
    "yandex_market": {"status": "active"}
}

def load_plugin(name):
    return {"plugin": name, "status": "loaded"}
