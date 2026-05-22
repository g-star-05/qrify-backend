from pydantic import BaseModel

from typing import Optional


# AUTH

class UserSignupSchema(
    BaseModel
):

    name: str

    email: str

    password: str


class UserLoginSchema(
    BaseModel
):

    email: str

    password: str


# QR

class QRSchema(
    BaseModel
):

    text: str

    color: Optional[str] = (
        "#000000"
    )

    background: Optional[str] = (
        "#ffffff"
    )


# TEMPLATE

class TemplateSchema(
    BaseModel
):

    name: str

    category: str

    description: str