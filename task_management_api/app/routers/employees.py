from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas
from ..crud import employee_crud

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return employee_crud.create_employee(db, employee)

@router.get("/", response_model=list[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return employee_crud.get_all_employees(db)

@router.get("/{employee_id}", response_model=schemas.EmployeeWithTasks)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    return employee_crud.get_employee_by_id(db, employee_id)
