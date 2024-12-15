from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])

class User(BaseModel):
    username:str
    password:str

@router.post("/login")
def login(user: User):
    return {"username": user.username}