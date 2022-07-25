import base64
import sys
import uuid
from datetime import datetime
from logging import getLogger

from fastapi import APIRouter

from src.app.models.schema.story_schemas import StoryResponse, PostStoryRequest, EditStoryRequest
from src.app.models.type.story_types import PublishScopeType, StoryStatusType

sys.path.append("..")
logger = getLogger(__name__)
story_router = APIRouter()


@story_router.get("/api/story/{diary_story_id}",
                  response_model=StoryResponse,
                  description="스토리 조회", )
async def get_story(diary_story_id: int) -> StoryResponse:
    with open('src/app/resources/dog.jpg', 'rb') as img:
        base64_string = base64.b64encode(img.read())

    mock_story = StoryResponse(
        diary_story_id=diary_story_id,
        story_publish_scope_type=PublishScopeType.ALL_TYPE,
        account_id=uuid.uuid4(),
        status=StoryStatusType.NORMAL,
        background_image=base64_string,
        story_text="text",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return mock_story


@story_router.post("/api/story",
                   response_model=StoryResponse,
                   description="스토리 등록", )
async def post_story(request: PostStoryRequest) -> StoryResponse:
    mock_story = StoryResponse(
        diary_story_id=100,
        story_publish_scope_type=request.story_publish_scope_type,
        account_id=request.account_id,
        status=StoryStatusType.NORMAL,
        background_image=request.background_image,
        story_text=request.background_image,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return mock_story


@story_router.put("/api/story",
                  response_model=StoryResponse,
                  description="스토리 수정", )
async def edit_story(request: EditStoryRequest) -> StoryResponse:
    mock_story = StoryResponse(
        diary_story_id=request.diary_story_id,
        story_publish_scope_type=request.story_publish_scope_type,
        account_id=request.account_id,
        status=StoryStatusType.NORMAL,
        background_image=request.background_image,
        story_text=request.background_image,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return mock_story


@story_router.delete("/api/story/{diary_story_id}",
                     description="스토리 삭제", )
async def delete_story(diary_story_id: int):
    return 'SUCCESS'
