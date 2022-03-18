from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

from .gender import Gender


# Shared properties
class OrderChangeTypeBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class OrderChangeTypeCreate(OrderChangeTypeBase):
    pass


# Properties to receive on item update
class OrderChangeTypeUpdate(OrderChangeTypeBase):
    pass


# Properties shared by models stored in DB
class OrderChangeTypeInDBBase(OrderChangeTypeBase):
    id: int
    nameRu: str
    nameKz: str

    class Config:
        orm_mode = True


# Properties to return to client
class OrderChangeType(OrderChangeTypeBase):
    id: int

    class Config:
        orm_mode = True


# Properties properties stored in DB
class OrderChangeTypeInDB(OrderChangeTypeInDBBase):
    pass

