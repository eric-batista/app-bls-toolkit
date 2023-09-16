import fastapi
from fastapi.responses import ORJSONResponse
from fastapi import status as http_status
from devtools.providers.database import AsyncDatabaseProvider
from src.core import database

router = fastapi.APIRouter()


@router.get('/health-check')
async def health_check(
    default_database: AsyncDatabaseProvider = fastapi.Depends(database.get_default_database)
):
    response = {
        "status": True,
        "database": await default_database.health_check(),
    }

    if not all(response.values()):
        return ORJSONResponse(
            response, status_code=http_status.HTTP_503_SERVICE_UNAVAILABLE
        )

    return response
