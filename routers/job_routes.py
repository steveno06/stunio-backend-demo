from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from database.config import get_db
from sqlalchemy.orm import Session
from database.job_repository import JobRepository
from models.job import Job



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
        return {"status": "success"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/all")
def get_all_jobs(db: Session = Depends(get_db)):
    job_repo = JobRepository(db)
    jobs = job_repo.getJobs()
    return jobs



