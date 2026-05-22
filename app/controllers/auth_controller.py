from fastapi import HTTPException
from passlib.context import CryptContext

# PASSWORD HASHING

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# TEMP STORAGE
# Later replace with MongoDB

users_db = []


# SIGNUP FUNCTION

def signup_user(user):

    # CHECK EXISTING EMAIL

    existing_user = next(
        (
            u for u in users_db
            if u["email"] == user.email
        ),
        None
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # HASH PASSWORD

    hashed_password = pwd_context.hash(
        user.password
    )

    new_user = {

        "name":
        user.name,

        "email":
        user.email,

        "password":
        hashed_password
    }

    users_db.append(
        new_user
    )

    return {

        "message":
        "User registered successfully",

        "user":
        {
            "name":
            user.name,

            "email":
            user.email
        }
    }


# LOGIN FUNCTION

def login_user(user):

    existing_user = next(
        (
            u for u in users_db
            if u["email"] == user.email
        ),
        None
    )

    if not existing_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # VERIFY PASSWORD

    valid_password = (
        pwd_context.verify(
            user.password,
            existing_user["password"]
        )
    )

    if not valid_password:

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    return {

        "message":
        "Login successful",

        "user":
        {
            "name":
            existing_user["name"],

            "email":
            existing_user["email"]
        }
    }