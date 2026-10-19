from .database import Base
from sqlalchemy import Column, Integer, String, Float

class Employee(Base):
    __tablename__="employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    designation = Column(String(50), nullable=False)
    salary = Column(Float, nullable=False)