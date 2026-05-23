from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager


# ROUTES

from app.routes.auth_routes import (
    router as auth_router
)

from app.routes.qr_routes import (
    router as qr_router
)

from app.routes.template_routes import (
    router as template_router
)

from app.routes.media_routes import (
    router as media_router
)

# NEW

from app.routes.upload_routes import (
    router as upload_router
)


# DATABASE

from app.database.connection import (
    test_connection
)



@asynccontextmanager
async def lifespan(
    app: FastAPI
):

    # STARTUP

    test_connection()

    yield

    # SHUTDOWN

    pass



app = FastAPI(

    title="QRify API",

    lifespan=lifespan

)



# CORS

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "https://qrify-49bm.onrender.com",

        "http://localhost:5173"

    ],

    allow_credentials=False,

    allow_methods=["*"],

    allow_headers=["*"],

    expose_headers=["*"]

)



# STATIC

app.mount(

    "/static",

    StaticFiles(

        directory="app/static"

    ),

    name="static"

)



# HOME

@app.get("/")

def home():

    return {

        "message":

        "QRify Backend Running 🚀"

    }



# ROUTERS

app.include_router(
    auth_router
)

app.include_router(
    qr_router
)

app.include_router(
    template_router
)

app.include_router(
    media_router
)

# NEW UPLOAD ROUTE

app.include_router(
    upload_router
)