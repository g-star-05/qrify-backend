from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from fastapi.staticfiles import (
    StaticFiles
)

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

# DATABASE

from app.database.connection import (
    test_connection
)


app = FastAPI(

    title="QRify API"

)

# DATABASE CONNECTION

test_connection()

# STATIC FILES

app.mount(

    "/static",

    StaticFiles(

        directory="app/static"

    ),

    name="static"

)

# CORS

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "https://qrify-49bm.onrender.com",

        "http://localhost:5173"

    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

# HOME ROUTE

@app.get("/")

def home():

    return {

        "message":

        "QRify Backend Running 🚀"

    }


# ROUTES

app.include_router(

    auth_router

)

app.include_router(

    qr_router

)

app.include_router(

    template_router

)