from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def init_migrations():
    return {"Message": "Initialization Complete"}