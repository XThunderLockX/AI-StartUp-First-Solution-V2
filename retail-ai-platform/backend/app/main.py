from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .api.v1.router import api_router

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])  # container liveness
async def health() -> dict:
    return {"status": "ok"}


@app.get("/hello", tags=["hello"])  # simple direct route
async def hello() -> dict:
    return {"message": "Hello from Retail AI Backend"}


app.include_router(api_router, prefix="/api/v1")
