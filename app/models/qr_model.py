from pydantic import BaseModel
from typing import Optional


class QRModel(
    BaseModel
):

    text: str

    color: Optional[str] = (
        "#000000"
    )

    background: Optional[str] = (
        "#ffffff"
    )