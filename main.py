from typing import List
from fastapi import FastAPI
from models import User, Gender, Role
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Shailendra"}
