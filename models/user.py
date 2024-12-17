from pydantic import BaseModel

class UserLogin(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    message: str
    user_id: int

class UserRegister(BaseModel):
    username: str
    password: str

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    user_type: str

class StudentRegistration(UserBase):
    school: str
    major: str
    graduation_year: int

class BusinessRegistration(UserBase):
    company_name: str
    industry: str
    business_size: int