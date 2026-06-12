import sys
from ecos.main import run_command

if __name__ == "__main__":
    run_command(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv)>3 else None)
