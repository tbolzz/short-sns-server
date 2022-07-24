from uuid import UUID

from pydantic import BaseModel
from datetime import datetime
from src.app.models.type.story_types import PublishScopeType, StoryStatusType


class PostStoryRequest(BaseModel):
    story_publish_scope_type: PublishScopeType
    account_id: UUID
    background_image: str
    story_text: str


class EditStoryRequest(BaseModel):
    diary_story_id: int
    story_publish_scope_type: PublishScopeType
    account_id: UUID
    background_image: str
    story_text: str


class StoryResponse(BaseModel):
    diary_story_id: int
    story_publish_scope_type: PublishScopeType
    account_id: UUID
    status: StoryStatusType
    background_image: str
    story_text: str
    created_at: datetime
    updated_at: datetime
