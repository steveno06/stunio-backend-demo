from typing import Union
from fastapi import FastAPI, Depends
from routers import user_routes
from sqlalchemy.orm import Session
from database.config import get_db, engine
from models import user_model

user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def test_root(db: Session = Depends(get_db)):
    return {"hello":"hello"}

app.include_router(user_routes.router)