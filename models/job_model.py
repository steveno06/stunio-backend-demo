from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from database.config import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey("users.id"), index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    required_students = Column(Integer, nullable=False)
    event_date = Column(Date,nullable=False)
    is_booked = Column(bool, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    business = relationship("User", backref="business_profile")

class JobInvite(Base):
    __tablename__ = "job_invites"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), index=True)
    student_id = Column(Integer, ForeignKey("users.id"), index=True)
    has_accepted = Column(bool, default=False)

    job = relationship("Job", backref="invites")
    student = relationship("User", backref='job_invites')
    