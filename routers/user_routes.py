from fastapi import APIRouter
from models.user import UserLogin

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/login")
def login(user: UserLogin):
    return {"username": user.username}