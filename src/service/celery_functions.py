# Third Party Library
from fastapi import status
from fastapi.responses import ORJSONResponse

# Project Stuff
from apps.celery_app import celery


def get_orjson_response(task) -> ORJSONResponse:
    return ORJSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"task_id": task.id})


def get_task_result(task_id: str):
    return celery.AsyncResult(task_id)
