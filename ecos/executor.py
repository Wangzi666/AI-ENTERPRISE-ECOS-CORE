from ecos.runtime.sprint_runtime import SprintRuntime
from ecos.builder import Builder

class Executor:

    def __init__(self):
        self.runtime = SprintRuntime()
        self.builder = Builder()

    def build(self, entity, target):
        print("рџљЂ ECOS BUILD START")
        plan = self.runtime.resolve(entity, target)
        self.builder.generate(plan)
        print("вњ… BUILD COMPLETE")
