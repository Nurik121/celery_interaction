# Third Party Library
from pydantic import RedisDsn
from pydantic import Field
# Project Stuff
from core.base_config import MixinSettings


class CeleryConfig(MixinSettings):
    celery_broker_url: RedisDsn = Field(default='redis://localhost:6379', env="REDIS_DSN")
    celery_result_backend: RedisDsn = Field(default='redis://localhost:6379', env="REDIS_DSN")


celery_config = CeleryConfig()
