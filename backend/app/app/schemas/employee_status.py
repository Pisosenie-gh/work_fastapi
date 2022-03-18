from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

from .gender import Gender


# Shared properties
class EmployeeStatusBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class EmployeeStatusCreate(EmployeeStatusBase):
    pass


# Properties to receive on item update
class EmployeeStatusUpdate(EmployeeStatusBase):
    pass


# Properties shared by models stored in DB
class EmployeeStatusInDBBase(EmployeeStatusBase):
    id: int
    nameRu: str
    nameKz: str

    class Config:
        orm_mode = True


# Properties to return to client
class EmployeeStatus(EmployeeStatusBase):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties properties stored in DB
class EmployeeStatusInDB(EmployeeStatusInDBBase):
    pass

