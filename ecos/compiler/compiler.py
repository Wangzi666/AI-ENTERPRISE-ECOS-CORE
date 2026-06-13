class SprintCompiler:

    def compile(self, sprint: str):
        return {
            "ast": {
                "type": "SPRINT",
                "name": sprint,
                "nodes": [
                    {"op": "resolve_dependencies"},
                    {"op": "build_graph"},
                    {"op": "execute"}
                ]
            }
        }
