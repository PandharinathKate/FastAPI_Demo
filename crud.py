# crud.py
from sqlalchemy.orm import Session
from Models import *
from Schemas import *

def get_employee(db: Session):
    return db.query(Employee).all()

def get_employeebyid(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()

def create_employee(db : Session, emp : EmployeeCreate):
    db_emp = Employee(Name = emp.Name, Salary = emp.Salary, Department = emp.Department)
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def update_employee(db : Session, empid : int, emp : EmployeeCreate):
    db_employee = db.query(Employee).filter(Employee.Id == empid).first()

    db_employee.Name = emp.Name
    db_employee.Salary = emp.Salary
    db_employee.Department = emp.Department

    db.commit()
    db.refresh(db_employee)

    return db_employee

def delete_employee(db : Session, empid : int):
    db_employee = db.query(Employee).filter(Employee.Id == empid).first()

    if db_employee is None:
        return "Employee does not exists!"
    
    db.delete(db_employee)
    db.commit()

    return db_employee