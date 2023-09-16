from devtools.config import Config
from devtools.providers.config import from_env
from devtools.providers.database import DatabaseConfig, Driver
import pathlib

config = Config()

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE_DIR = ROOT.parent

BASE_PATH = config("BASE_PATH", str)
ENV = config("ENV", str)

DEFAULT_DATABASE = "database"
DB_DRIVER = config("DB_DRIVER", Driver, Driver.POSTGRES)
default_database = from_env(
    DatabaseConfig,
    driver=DB_DRIVER
)
