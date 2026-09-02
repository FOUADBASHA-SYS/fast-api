from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import engine, Base
from app.routers import auth_router, home_router
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
        print(">> Ensure your database is running and DATABASE_URL is configured in .env")
    yield


app = FastAPI(
    title=settings.APP_NAME,
    description="High-Performance REST API Backend with JWT Authentication and PostgreSQL/SQLite Database.",
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

# Include Routers
app.include_router(auth_router)
app.include_router(home_router)


@app.get("/", tags=["General"], summary="API Root Overview")
def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "online",
        "docs": "/docs",
        "redoc": "/redoc",
        "endpoints": {
            "register": "POST /api/auth/register",
            "login": "POST /api/auth/login",
            "profile": "GET /api/home/me",
            "health": "GET /api/health"
        }
    }


@app.get("/api/health", tags=["General"], summary="Health Check")
def health_check():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
