# Third Party Library
from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

from service.celery_functions import get_orjson_response
from tasks.history_predict import celery_test
router = APIRouter(prefix='/test', tags=['test'])


@router.post("/test", status_code=status.HTTP_202_ACCEPTED)
def test_api(
    test: str,
) -> ORJSONResponse:
    task = celery_test.delay({'test':test})
    return get_orjson_response(task=task)

