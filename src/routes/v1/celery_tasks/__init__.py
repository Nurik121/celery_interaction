# Third Party Library
from fastapi import APIRouter

# Project Stuff
from routes.v1.celery_tasks.celery_health_check import router as health_router
from routes.v1.celery_tasks.celery_history_predict import (
    router as history_predict_router,
)

router = APIRouter(prefix='/celery')

router.include_router(history_predict_router)
router.include_router(health_router)
