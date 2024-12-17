from pydantic import BaseModel

class UserLogin(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    message: str
    user_id: int