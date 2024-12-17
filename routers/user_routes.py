from fastapi import APIRouter, Depends, HTTPException
from database.config import get_db
from sqlalchemy.orm import Session
from database.user_repository import UserRepository
from models.user import UserLogin, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/login")
def login(request: UserLogin, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_credentials(request.username, request.password)
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return UserResponse(message="Login Success", user_id=user.id)