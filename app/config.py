import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "XDR Security Platform - El Shorouk Academy"
    APP_VERSION: str = "2.0.0"
    DEBUG: bool = True

    # Database URL (supports SQLite / PostgreSQL)
    DATABASE_URL: str = "sqlite:///./portal.db"

    # JWT Settings
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # Wazuh API Integration Settings
    WAZUH_API_URL: str = "https://localhost:55000"
    WAZUH_API_USERNAME: str = "wazuh-wui"
    WAZUH_API_PASSWORD: str = "wazuh-wui"
    WAZUH_VERIFY_SSL: bool = False
    WAZUH_REQUEST_TIMEOUT: float = 8.0

    # CORS Configuration
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://localhost:8000"
    ]

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
