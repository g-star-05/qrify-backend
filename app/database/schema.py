from pydantic import BaseModel
from typing import Optional


# =========================
# AUTH SCHEMA
# =========================

class UserSignupSchema(BaseModel):

    name: str

    email: str

    password: str


class UserLoginSchema(BaseModel):

    email: str

    password: str


# =========================
# QR SCHEMA
# =========================

class QRSchema(BaseModel):

    text: str

    color: Optional[str] = "#000000"

    background: Optional[str] = "#ffffff"


# =========================
# TEMPLATE SCHEMA
# =========================

class TemplateSchema(BaseModel):

    name: str

    category: str

    description: str


# =========================
# RESPONSE SCHEMA
# =========================

class ResponseSchema(BaseModel):

    message: str