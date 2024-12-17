from sqlalchemy import Column, Integer, String, Enum
from database.config import Base
import enum

class UserType(enum.Enum):
    STUDENT = "STUDENT"
    BUSINESS = "BUSINESS"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True)
    user_type = Column(Enum(UserType))