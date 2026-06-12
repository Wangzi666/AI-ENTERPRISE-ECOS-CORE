class EventBus:
    def __init__(self):
        self.events = []

    def emit(self, event_type, payload):
        self.events.append({
            "type": event_type,
            "payload": payload
        })
        return {"status": "event emitted", "type": event_type}
