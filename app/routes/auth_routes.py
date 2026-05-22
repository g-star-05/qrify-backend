from fastapi import APIRouter

from app.models.user_model import (
    UserModel,
    LoginModel
)

from app.controllers.auth_controller import (
    signup_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# SIGNUP

@router.post(
    "/signup"
)

def signup(
    user: UserModel
):

    return signup_user(
        user
    )


# LOGIN

@router.post(
    "/login"
)

def login(
    user: LoginModel
):

    return login_user(
        user
    )