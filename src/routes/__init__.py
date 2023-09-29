# Third Party Library
from fastapi import APIRouter

# Project Stuff
from routes.v1 import router as v1_router

router = APIRouter(prefix='/api')
router.include_router(v1_router)
