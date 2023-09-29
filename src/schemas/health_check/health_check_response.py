# Standard Library
from typing import Literal

# Third Party Library
from pydantic import BaseModel, NonNegativeInt


class HealthCheckResponse(BaseModel):
    date_time: str
    status_code: NonNegativeInt
    status_message: Literal["Good"]
