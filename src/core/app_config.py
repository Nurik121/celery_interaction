# Third Party Library
from pydantic import PositiveInt
from pydantic import Field
# Project Stuff
from core.base_config import MixinSettings


class AppConfig(MixinSettings):
    service_host: str = Field(..., env="HOST")
    service_port: PositiveInt = Field(..., env="PORT")


app_config: AppConfig = AppConfig()
