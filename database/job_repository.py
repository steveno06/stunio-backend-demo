from sqlalchemy import Date
from sqlalchemy.orm import Session
from models.job_model import Job, JobInvite

class JobRepository:
    def __init__(self, db: Session):
        self.db = db

    def createJob(self, title : str, description : str, business_id : int, required_students : int, event_date: Date):
        new_job = Job(
            title = title,
            description = description,
            business_id = business_id,
            required_students = required_students,
            event_date = event_date
        )

        self.db.add(new_job)
        self.db.commit()
        self.db.refresh(new_job)
    
    def getJobs(self):
        return self.db.query(Job).all()