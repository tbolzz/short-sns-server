import sys
from logging import getLogger
from fastapi import APIRouter

sys.path.append("..")
logger = getLogger(__name__)
router = APIRouter()


@router.get("/api/hello")
async def hello():
    return 'FastAPI!'
