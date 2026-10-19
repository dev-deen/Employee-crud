from .models import Employee
from .schemas import EmployeeCreate, EmployeeUpdate
from sqlalchemy.orm import Session

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(
        Employee.id == employee_id 
    ).first()

def get_all_employees(db: Session):
    return db.query(Employee).all()

def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, employee_id: int, employee_update: EmployeeUpdate):
    db_employee = get_employee_by_id(db, employee_id)
    if not db_employee:
        return None
    
    for key, value in employee_update.model_dump(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee_by_id(db, employee_id)
    if not db_employee:
        return None
    db.delete(db_employee)
    db.commit()
    return True