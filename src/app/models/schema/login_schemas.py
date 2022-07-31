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


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str
