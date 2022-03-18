from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

# Shared properties
class GenderBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class GenderCreate(GenderBase):
    pass


# Properties to receive on item update
class GenderUpdate(GenderBase):
    pass


# Properties shared by models stored in DB
class GenderInDBBase(GenderBase):
    id: int
    nameRu: str
    nameKz: str
    class Config:
        orm_mode = True


# Properties to return to client
class Gender(GenderBase):
    id: int
    class Config:
        orm_mode = True

# Properties properties stored in DB
class GenderInDB(GenderInDBBase):
    pass

