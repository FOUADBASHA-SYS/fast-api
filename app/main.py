import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import engine, Base
from app.routers import auth_router, home_router, pages_router
# Ensure models are imported so Base metadata knows all tables
import app.models.user


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables on startup
    try:
        Base.metadata.create_all(bind=engine)
        print(">> Database tables initialized successfully.")
    except Exception as e:
        print(f">> Notice: Could not automatically connect/create tables: {e}")
        print(">> Ensure PostgreSQL is running and DATABASE_URL is configured in .env")
    yield


app = FastAPI(
    title=settings.APP_NAME,
    description="Full-stack FastAPI + PostgreSQL Authentication Backend with Home, Login, and Registration pages.",
    version=settings.APP_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Static Files
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Include Routers
app.include_router(auth_router)
app.include_router(home_router)
app.include_router(pages_router)


@app.get("/api/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
