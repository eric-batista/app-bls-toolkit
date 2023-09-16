import fastapi
from fastapi.responses import ORJSONResponse

from src import __version__
from src.core import settings, events, database
from src.routes import router


def get_application():

    application = fastapi.FastAPI(
        default_response_class=ORJSONResponse,
        version=__version__,
        docs_url=f"{settings.BASE_PATH}/docs",
        redoc_url=f"{settings.BASE_PATH}/redoc",
        openapi_url=f"{settings.BASE_PATH}/openapi.json"
    )

    application.add_event_handler(
        "startup",
        events.on_event(
            application,
            database.initialize_database()
        )
    )

    application.include_router(router, prefix=f"{settings.BASE_PATH}")

    return application


app = get_application()
