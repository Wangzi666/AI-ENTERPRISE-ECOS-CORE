from ecos.compiler.compiler import SprintCompiler
from ecos.runtime.graph.graph import ExecutionGraph

class FactoryCore:

    def build(self, sprint):
        compiler = SprintCompiler()
        plan = compiler.compile(sprint)

        graph = ExecutionGraph(plan["ast"])
        graph.run()
