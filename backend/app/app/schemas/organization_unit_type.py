from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

from .gender import Gender


# Shared properties
class OrganizationUnitTypeBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class OrganizationUnitTypeCreate(OrganizationUnitTypeBase):
    pass

# Properties to receive on item update
class OrganizationUnitTypeUpdate(OrganizationUnitTypeBase):
    pass


# Properties shared by models stored in DB
class OrganizationUnitTypeInDBBase(OrganizationUnitTypeBase):
    id: int
    nameRu: str
    nameKz: str


    class Config:
        orm_mode = True


# Properties to return to client
class OrganizationUnitType(OrganizationUnitTypeBase):
    id: int
 

    class Config:
        orm_mode = True


# Properties properties stored in DB
class OrganizationUnitTypeInDB(OrganizationUnitTypeInDBBase):
    pass

