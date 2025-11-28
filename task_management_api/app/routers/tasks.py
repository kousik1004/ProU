from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from .. import schemas, models
from ..auth import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/", response_model=List[schemas.TaskResponse])
def get_tasks(
    status: Optional[str] = None,
    employee_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Task)

    if status:
        query = query.filter(models.Task.status == status)

    if employee_id:
        query = query.filter(models.Task.employee_id == employee_id)

    return query.all()

@router.get("/{task_id}", response_model=schemas.TaskResponse)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user) 
):
    # Check if employee exists
    employee = db.query(models.Employee).filter(models.Employee.id == task.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    new_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status,
        employee_id=task.employee_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    updated_task: schemas.TaskUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user) 
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if updated_task.title is not None:
        task.title = updated_task.title

    if updated_task.description is not None:
        task.description = updated_task.description

    if updated_task.status is not None:
        task.status = updated_task.status

    if updated_task.employee_id is not None:
        employee = db.query(models.Employee).filter(models.Employee.id == updated_task.employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        task.employee_id = updated_task.employee_id

    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
