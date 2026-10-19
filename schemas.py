from pydantic import BaseModel, Field, ConfigDict, NonNegativeFloat
from typing import List, Optional
class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=18, le=65)
    department: str = Field(..., min_length=2, max_length=50)
    designation: str = Field(..., min_length=2, max_length=50)
    salary: NonNegativeFloat = Field(..., example=50000.0)

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    age: Optional[int] = Field(None, ge=18, le=65)
    department: Optional[str] = Field(None, min_length=2, max_length=50)
    designation: Optional[str] = Field(None, min_length=2, max_length=50)
    salary: Optional[NonNegativeFloat] = Field(None, example=50000.0)

class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
