from sqlalchemy import Date
from sqlalchemy.orm import Session
from models.job_model import Job, JobInvite
from models.student_model import Student
from sqlalchemy.sql.expression import func

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

        avalaible_students = self.get_avaliable_students(num_of_students=required_students, date=event_date)
        self.invite_students(students=avalaible_students, job_id=new_job.id)
        
        return new_job
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
    
    def get_avaliable_students(self, num_of_students : int, date: Date):
        
        #Find students who are not available for given date
        unavailable_students = (
            self.db.query(JobInvite.student_id)
            .join(Job, JobInvite.job_id == Job.id)
            .filter(JobInvite.has_accepted == True, Job.event_date == date)
            .distinct()
            .all()
        )

        unavailable_students_ids = [student[0] for student in unavailable_students]

        #Find all students who are avaible for given date
        available_students = (
            self.db.query(Student)
            .filter(~Student.id.in_(unavailable_students_ids))
            .order_by(func.random())
            .limit(num_of_students)
            .all()
        )

        return available_students

    def invite_students(self, students: list[Student], job_id : int):
        try:
            for student in students:
                self.createJobInvite(job_id=job_id, student_id=student.id)
            return True
        except Exception as e:
            self.db.rollback()
            return False