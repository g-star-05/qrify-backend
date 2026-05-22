from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Routes
from app.routes.auth_routes import router as auth_router
from app.routes.qr_routes import router as qr_router
from app.routes.template_routes import router as template_router

# Database
from app.database.connection import test_connection

app = FastAPI(title="QRify API")

# -------------------------------------------------------
# FIX 1: CORS must be added BEFORE mounting static files
# and BEFORE including routers — middleware order matters
# in FastAPI/Starlette. If added after, preflight OPTIONS
# requests won't get CORS headers and the browser blocks them.
# -------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://qrify-49bm.onrender.com",
        "http://localhost:5173",
    ],
    # FIX 2: Removed "*" from allow_origins.
    # You cannot mix specific origins with "*" — it causes
    # unpredictable CORS behaviour. Since you have specific
    # origins listed, just use those. If you need to allow
    # all origins, replace the list with just ["*"] but then
    # allow_credentials must stay False.
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# -------------------------------------------------------
# FIX 3: Database connection should be wrapped in a
# lifespan event, not called at module level.
# Calling test_connection() at import time means it runs
# before the app is fully initialised and any error will
# crash the entire startup with no useful context.
# -------------------------------------------------------
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    test_connection()
    yield
    # Shutdown (add cleanup logic here if needed)

# Re-create app with lifespan
app = FastAPI(title="QRify API", lifespan=lifespan)

# Re-add middleware after re-creating app
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://qrify-49bm.onrender.com",
        "http://localhost:5173",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

# Home route
@app.get("/")
def home():
    return {"message": "QRify Backend Running 🚀"}

# Routers
app.include_router(auth_router)
app.include_router(qr_router)
app.include_router(template_router)
