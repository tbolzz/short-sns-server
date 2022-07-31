from logging import getLogger
from fastapi import FastAPI

from src.app.routers.story import story_router
from src.app.routers.login import login_router

logger = getLogger(__name__)

app = FastAPI(
    title="short-sns",
    description="fastAPI mock",
    version="0.0.1",
)

app.include_router(story_router.story_router, prefix="", tags=[""])
app.include_router(login_router.login_router, prefix="", tags=[""])
