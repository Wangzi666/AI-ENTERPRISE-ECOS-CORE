class ExecutionGraph:

    def __init__(self, ast):
        self.ast = ast

    def run(self):
        for node in self.ast["nodes"]:
            print("⚙️ EXEC:", node["op"])
