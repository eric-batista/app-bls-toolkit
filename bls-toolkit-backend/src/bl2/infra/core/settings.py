from devtools.config import Config

config = Config()


ROOT_PATH = config("BASE_PATH", str)
BASE_PATH_BL2 = config("BASE_PATH_BL2", str, default="/bl2")

ROUTER_BASE_PATH = ROOT_PATH + BASE_PATH_BL2

print(ROUTER_BASE_PATH)
