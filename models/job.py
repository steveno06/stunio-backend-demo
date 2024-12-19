from pydantic import BaseModel

class Job(BaseModel):
    user_id: int
    title: str
    description: str | None
    required_students: int
    event_date: str

class Invite(BaseModel):
    invite_id : int