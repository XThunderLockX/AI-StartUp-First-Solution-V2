from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...dependencies import get_db
from ...core.cache import redis_client
from .endpoints.auth import router as auth_router
from .endpoints.products import router as products_router
from .endpoints.inventory import router as inventory_router

api_router = APIRouter()


@api_router.get("/health", tags=["health"])
async def api_health() -> dict:
    return {"status": "ok"}


@api_router.get("/hello", tags=["hello"])
async def api_hello() -> dict:
    return {"message": "Hello from API v1"}


@api_router.get("/db-check", tags=["health"])  # rudimentary check
async def db_check(db: Session = Depends(get_db)) -> dict:
    try:
        db.execute("SELECT 1")
        return {"database": "ok"}
    except Exception as exc:  # pragma: no cover
        return {"database": f"error: {exc}"}


@api_router.get("/redis-check", tags=["health"])  # rudimentary check
async def redis_check() -> dict:
    try:
        redis_client.ping()
        return {"redis": "ok"}
    except Exception as exc:  # pragma: no cover
        return {"redis": f"error: {exc}"}


api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(products_router, prefix="/products", tags=["products"])
api_router.include_router(inventory_router, prefix="/inventory", tags=["inventory"])
