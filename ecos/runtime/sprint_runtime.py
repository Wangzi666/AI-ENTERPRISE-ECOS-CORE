class SprintRuntime:

    def resolve(self, entity, target):
        return {
            "entity": entity,
            "target": target,
            "tasks": [
                "api",
                "docker",
                "git"
            ]
        }


