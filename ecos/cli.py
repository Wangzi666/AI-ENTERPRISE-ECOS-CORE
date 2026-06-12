import sys
from ecos.compiler.sprint_compiler import SprintCompiler

def main():
    if len(sys.argv) < 3:
        print("Usage: ecos build sprint <version>")
        return

    command = sys.argv[1]
    entity = sys.argv[2]      # sprint
    target = sys.argv[3]      # 2.1 / 3 / 10

    if command == "build":
        compiler = SprintCompiler()
        compiler.run(entity, target)

if __name__ == "__main__":
    main()