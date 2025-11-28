from sqlalchemy.orm import Session
from fastapi import HTTPException
from .. import models, schemas

def create_task(db: Session, task: schemas.TaskCreate):
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

def get_all_tasks(db: Session, status: str = None, employee_id: int = None):
    query = db.query(models.Task)
    if status:
        query = query.filter(models.Task.status == status)
    if employee_id:
        query = query.filter(models.Task.employee_id == employee_id)
    return query.all()

def update_task(db: Session, task_id: int, updates: schemas.TaskUpdate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
