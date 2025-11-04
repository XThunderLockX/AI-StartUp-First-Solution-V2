from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
async def login() -> dict:
    return {"access_token": "placeholder", "token_type": "bearer"}
