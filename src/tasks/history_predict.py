# Project Stuff
from apps.celery_app import celery


@celery.task(name='celery_test')
def celery_test(test: dict) -> dict:
    return test
