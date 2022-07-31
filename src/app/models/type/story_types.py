from enum import Enum


class PublishScopeType(Enum):
    ALL_TYPE = 'ALL'
    ONLY_FOLLOWER = 'ONLY_FOLLOWER'
    SPECIFIC_USER = 'SPECIFIC_USER'
    NO_ONE = 'NO_ONE'


class StoryStatusType(Enum):
    NORMAL = 'NORMAL'
    DELETED = 'DELETED'
    HIDE = 'HIDE'
