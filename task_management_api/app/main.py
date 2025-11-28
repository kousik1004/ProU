import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
from .database import Base, engine
from .routers import employees, tasks
from .routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="Backend task for ProU Technology Internship",
    version="1.0.0"
)

app.include_router(employees.router)
app.include_router(tasks.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Task Management API is running!"}
