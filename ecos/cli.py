import sys
from ecos.core.factory_core import FactoryCore

if __name__ == "__main__":
    factory = FactoryCore()
    factory.build(sys.argv[1])
