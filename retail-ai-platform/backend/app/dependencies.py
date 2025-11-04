from typing import Generator
from .config import settings as app_settings
from .core.database import SessionLocal


def get_settings():
    return app_settings


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
