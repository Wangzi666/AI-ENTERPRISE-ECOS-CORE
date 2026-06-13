from ecos.executor import Executor

def run_command(command, entity, target):
    executor = Executor()
    if command == "build":
        executor.build(entity, target)


