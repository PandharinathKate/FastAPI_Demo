# models.py
from sqlalchemy import Column, Integer, String
from database import Base

# Example User model
class Employee(Base):
    __tablename__ = "employee"
    
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100))
    Salary = Column(Integer)
    Department = Column(String(50))
