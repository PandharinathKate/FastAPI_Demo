from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import *
from database import engine
from dependencies import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/employees")
def GetEmployees(db : Session = Depends(get_db)):
    return get_employee(db)

@app.get("/employees/{id}")
def GetEmployeesById(id : int, db : Session = Depends(get_db)):
    return get_employeebyid(db, id)

@app.post("/employee/", response_model=EmployeeResponse)
def CreateEmployee(employee : EmployeeCreate, db : Session = Depends(get_db)):
    return create_employee(emp = employee, db = db)

@app.put("/employee/", response_model=EmployeeResponse)
def UpdateEmployee(empid : int, employee : EmployeeCreate, db : Session = Depends(get_db)):
    return update_employee(empid=empid, emp=employee, db=db)

@app.delete("/employee/{empid}")
def DeleteEmployee(empid : int, db : Session = Depends(get_db)):
    return delete_employee(empid=empid, db=db)
