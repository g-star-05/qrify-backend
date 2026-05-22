import jwt

from fastapi import (
    HTTPException,
    Header
)

import os

from dotenv import load_dotenv

# LOAD ENV

load_dotenv()

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "qrify_secret"
)

ALGORITHM = "HS256"


# VERIFY TOKEN

def verify_token(
    authorization: str = Header(None)
):

    if not authorization:

        raise HTTPException(

            status_code=401,

            detail=
            "Authorization token missing"
        )

    try:

        # REMOVE "Bearer"

        token = authorization.replace(
            "Bearer ",
            ""
        )

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[
                ALGORITHM
            ]
        )

        return payload

    except jwt.ExpiredSignatureError:

        raise HTTPException(

            status_code=401,

            detail=
            "Token expired"
        )

    except jwt.InvalidTokenError:

        raise HTTPException(

            status_code=401,

            detail=
            "Invalid token"
        )