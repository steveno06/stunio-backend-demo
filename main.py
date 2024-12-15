from typing import Union
from fastapi import FastAPI
from routers import user_routes
app = FastAPI()

@app.get("/")
def test_root():
    return {"hello":"hello"}

app.include_router(user_routes.router)