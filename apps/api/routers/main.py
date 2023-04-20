from fastapi import APIRouter

router = APIRouter(
    tags=['meta']
)


@router.get("/")
async def index():
    return {"message": "Store API"}


@router.get("/health")
async def health():
    return {"message": "OK"}
