import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Auth Portal"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # PostgreSQL Database URL
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/fastapi_db"

    # JWT Settings
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
