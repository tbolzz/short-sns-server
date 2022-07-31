from typing import Union
from pydantic import BaseModel

fake_users_db = {
    "naru": {
        "username": "naru",
        "full_name": "CHOI naru",
        "hashed_password": "fakehashedsecret",
        "disabled": False
    },
    "P": {
        "username": "P",
        "full_name": "PARK P",
        "hashed_password": "fakehashedsecret2",
        "disabled": True
    }
}

fake_users_db2 = {
    "naru": {
        "username": "naru",
        "full_name": "CHOI naru",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str
