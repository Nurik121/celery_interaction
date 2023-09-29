# Third Party Library
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

# Project Stuff
from service.celery_functions import get_orjson_response, get_task_result
from tasks.health_check import celery_ping

router = APIRouter(prefix='/health', tags=['Celery Health Check'])


@router.get("/ping")
def ping_route(delay: int) -> ORJSONResponse:
    task = celery_ping.delay(delay)
    return get_orjson_response(task=task)


@router.get("/task_result")
def task_result_route(task_id: str):
    task_result = get_task_result(task_id)
    if task_result.status == "SUCCESS":
        return task_result.result
    return task_result.status
