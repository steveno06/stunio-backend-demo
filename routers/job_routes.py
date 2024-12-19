from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from database.config import get_db
from sqlalchemy.orm import Session
from database.job_repository import JobRepository
from models.job import Job, Invite



router = APIRouter(prefix='/jobs', tags=['jobs'])

@router.post("/create")
def create_job(request: Job, db: Session = Depends(get_db)):
    job_repo = JobRepository(db)
    try:
        event_date = datetime.strptime(request.event_date, "%d-%m-%Y").date()
    
        job_repo.createJob(
            title=request.title,
            description=request.description,
            business_id=request.user_id,
            required_students=request.required_students,
            event_date=event_date
        )

        job_repo.createJobInvite(job_id=1, student_id=1)
        return {"status": "success"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/accept")
def accept_job(request: Invite, db: Session = Depends(get_db)):
    job_repo = JobRepository(db)
    success = job_repo.acceptJobInvite(request.invite_id)

    if success:
        return {"status": "job accepted"}
    
@router.post("/decline")
def accept_job(request: Invite, db: Session = Depends(get_db)):
    job_repo = JobRepository(db)
    success = job_repo.declineJobInvite(request.invite_id)

    if success:
        return {"status": "job declined"}
    return {"status": "an error has occured"}

@router.get("/all")
def get_all_jobs(db: Session = Depends(get_db)):
    job_repo = JobRepository(db)
    jobs = job_repo.getJobs()
    return jobs

@router.get("/all-invites")
def get_all_invites(db: Session = Depends(get_db)):
    jobs_repo = JobRepository(db)
    invites = jobs_repo.getJobInvites()
    return invites



