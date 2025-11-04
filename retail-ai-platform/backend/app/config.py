from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "RetailAI"
    debug: bool = True
    secret_key: str = "CHANGE_ME"

    database_url: str = "postgresql://postgres:postgres@db:5432/retailai"
    redis_url: str = "redis://redis:6379"

    backend_cors_origins: List[str] = [
        "http://localhost:5173",
        "http://localhost:5174",
    ]
    access_token_expire_minutes: int = 30


settings = Settings()
