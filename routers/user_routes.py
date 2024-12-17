from fastapi import APIRouter, Depends, HTTPException
from database.config import get_db
from sqlalchemy.orm import Session
from database.user_repository import UserRepository
from models.user import UserLogin, UserResponse, StudentRegistration, BusinessRegistration

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/login")
def login(request: UserLogin, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_credentials(request.username, request.password)
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return UserResponse(message="Login Success", user_id=user.id)

@router.post("/register")
def register(request: dict, db: Session = Depends(get_db)):
    user_type = request.get("user_type")
    
    if user_type == "STUDENT":
        registration_model = StudentRegistration(**request)
    elif user_type == "BUSINESS":
        registration_model = BusinessRegistration(**request)
    else:
        raise HTTPException(status_code=400, detail="Invalid user_type")
    
    user_repo = UserRepository(db)
    reg_data = registration_model.model_dump()
    user = user_repo.register_user(registration_data=reg_data)
    
    if not user:
        raise HTTPException(status_code=401, detail="Registration failed")
    
    return UserResponse(message=f"{reg_data['user_type'].capitalize()} Registration Success", user_id=user.id)