from sqlalchemy.orm import Session
from models.user_model import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_by_credentials(self, username: str, password: str) -> User | None:
        return self.db.query(User).filter(
            User.username == username,
            User.password == password
        ).first()
    
    def register_user(self, usrname: str, passw: str):
        user = User(username=usrname, password=passw)
        self.db.add(user)
        self.db.commit()
        return user