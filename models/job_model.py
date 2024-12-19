from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from database.config import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(String)
    required_students = Column(Integer, nullable=False)
    event_date = Column(Date,nullable=False)
    is_booked = Column(bool, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    business = relationship("User", backref="business_profile")