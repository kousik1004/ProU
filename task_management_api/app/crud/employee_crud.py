from sqlalchemy.orm import Session
from fastapi import HTTPException
from .. import models, schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    existing = db.query(models.Employee).filter(models.Employee.email == employee.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_employee = models.Employee(
        name=employee.name,
        role=employee.role,
        email=employee.email
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_all_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee_by_id(db: Session, employee_id: int):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
