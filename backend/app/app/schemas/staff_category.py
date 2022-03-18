from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class StaffCategoryBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class StaffCategoryCreate(StaffCategoryBase):
    pass


# Properties to receive on item update
class StaffCategoryUpdate(StaffCategoryBase):
    pass


# Properties shared by models stored in DB
class StaffCategoryInDBBase(StaffCategoryBase):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class StaffCategory(StaffCategoryBase):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True

# Properties properties stored in DB
class StaffCategoryInDB(StaffCategoryInDBBase):
    pass

