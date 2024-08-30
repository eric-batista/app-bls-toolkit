import fastapi
from fastapi.responses import ORJSONResponse

from src.bl2 import __version__
from src.bl2.application.routes import router
from src.bl2.infra.core import settings


def get_application():
    application = fastapi.FastAPI(
        default_response_class=ORJSONResponse,
        version=__version__,
        docs_url=f"{settings.ROUTER_BASE_PATH}/docs",
        redoc_url=f"{settings.ROUTER_BASE_PATH}/redoc",
        openapi_url=f"{settings.ROUTER_BASE_PATH}/openapi.json",
    )

    application.include_router(router, prefix=f"{settings.ROUTER_BASE_PATH}")

    return application


app = get_application()
