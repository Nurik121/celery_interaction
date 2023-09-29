# Third Party Library
from fastapi import APIRouter

# Project Stuff
from routes.v1.celery_tasks import router as celery_router

router = APIRouter(prefix='/v1')

router.include_router(celery_router)
