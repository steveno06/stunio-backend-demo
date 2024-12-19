from sqlalchemy.orm import Session
from models.user_model import User, UserType
from models.student_model import Student
from models.business_model import Business

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_by_credentials(self, username: str, password: str) -> User | None:
        return self.db.query(User).filter(
            User.username == username,
            User.password == password
        ).first()
    
    def register_user(self, registration_data: dict) -> User | None:
        try:
            user = User(
                username=registration_data['username'],
                password=registration_data['password'],
                email=registration_data['email'],
                user_type=registration_data['user_type']
            )
            self.db.add(user)
            self.db.flush()

            if user.user_type == "STUDENT":
                print("student")
                student = Student(
                    user_id=user.id,
                    school=registration_data['school'],
                    major=registration_data['major'],
                    graduation_year= registration_data['graduation_year']
                )
                self.db.add(student)
                self.db.flush()
            
            elif user.user_type == "BUSINESS":
                business = Business(
                    user_id=user.id,
                    company_name=registration_data['company_name'],
                    industry=registration_data['industry'],
                    business_size=registration_data['business_size']
                )
                self.db.add(business)
                self.db.flush()

            self.db.commit()
            return user
        
        except Exception:
            self.db.rollback()
            return None