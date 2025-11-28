from pydantic import BaseModel, EmailStr
from typing import Optional, List

class EmployeeBase(BaseModel):
    name: str
    role: str
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "Pending"
    employee_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    employee_id: Optional[int] = None

class TaskResponse(TaskBase):
    id: int
    class Config:
        orm_mode = True

class EmployeeWithTasks(EmployeeResponse):
    tasks: List[TaskResponse] = []

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
