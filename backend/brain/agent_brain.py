class AgentBrain:
    def __init__(self, name, capabilities):
        self.name = name
        self.capabilities = capabilities

    def think(self, query):
        return {
            "agent": self.name,
            "thinking": f"Analyzing: {query}",
            "capabilities_used": self.capabilities
        }
