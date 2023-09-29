# Third Party Library
from celery import Celery
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Project Stuff
from core.celery_config import celery_config

celery = Celery(
    __name__,
    broker=celery_config.celery_broker_url,
    backend=celery_config.celery_result_backend,
    include=[
        "tasks.health_check",
        "tasks.history_predict",
    ],
)

celery.conf.timezone = 'UTC'
