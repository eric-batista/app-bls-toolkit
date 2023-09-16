
from devtools.providers.database import AsyncDatabaseProvider, Entity
from devtools.providers.database.api import make_provider_dependency, setup_databases


from src.core import settings

def initialize_database():
    return setup_databases(
        AsyncDatabaseProvider,
        (settings.DEFAULT_DATABASE, settings.default_database)
    )


DefaultEntity = Entity

get_default_database = make_provider_dependency(settings.DEFAULT_DATABASE)
