import sys
from ecos.executor import Executor

def main():
    if len(sys.argv) < 3:
        print("Usage: ecos build sprint_6")
        return

    command = sys.argv[1]
    target = sys.argv[2]

    executor = Executor()

    if command == "build":
        executor.build(target, "auto")

if __name__ == "__main__":
    main()

