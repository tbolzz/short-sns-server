from logging import getLogger
from fastapi import FastAPI

from src.app.routers import routers

logger = getLogger(__name__)

app = FastAPI(
    title="short-sns",
    description="fastAPI mock",
    version="0.0.1",
)

app.include_router(routers.router, prefix="", tags=[""])