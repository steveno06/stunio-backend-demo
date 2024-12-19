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
    
    def createJobInvite(self, job_id : int, student_id : int):
        new_job_invite = JobInvite(
            job_id = job_id,
            student_id=student_id,
        )

        self.db.add(new_job_invite)
        self.db.commit()
        self.db.refresh(new_job_invite)

    def acceptJobInvite(self, invite_id : int):
        student_invite = self.db.query(JobInvite).filter(JobInvite.id == invite_id).first()
        
        if not student_invite:
            return False
        
        student_invite.has_accepted = True
        self.db.commit()
        return True

    def declineJobInvite(self, invite_id : int):
        student_invite = self.db.query(JobInvite).filter(JobInvite.id == invite_id).first()

        if not student_invite:
            return False
        self.db.delete(student_invite)
        self.db.commit()
        return True

    def getJobInvites(self):
        return self.db.query(JobInvite).all()
