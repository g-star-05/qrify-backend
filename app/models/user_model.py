from pydantic import (
    BaseModel,
    EmailStr
)

from typing import Optional

from datetime import datetime


# USER MODEL

class UserModel(
    BaseModel
):

    name: str

    email: EmailStr

    password: str

    role: Optional[str] = "user"

    created_at: Optional[
        datetime
    ] = datetime.now()


# LOGIN MODEL

class LoginModel(
    BaseModel
):

    email: EmailStr

    password: str


# RESPONSE MODEL

class UserResponseModel(
    BaseModel
):

    id: int

    name: str

    email: EmailStr

    role: str

    created_at: datetime