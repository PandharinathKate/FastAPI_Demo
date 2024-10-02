from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    Name : str
    Salary : int
    Department : str

class EmployeeResponse(BaseModel):
    Id : int
    Name : str
    Salary : int
    Department : str

    class Config:
        orm_mode = True