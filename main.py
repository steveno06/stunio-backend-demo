from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test_root():
    return {"hello":"hello"}