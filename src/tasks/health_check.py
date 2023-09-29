# Standard Library
from time import sleep

# Project Stuff
from apps.celery_app import celery


@celery.task(name='celery_ping')
def celery_ping(delay: int):
    sleep(delay)
    return "Pong"
