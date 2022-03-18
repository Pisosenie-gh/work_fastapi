from typing import Optional

from pydantic import BaseModel, Field
from datetime import date

from .gender import Gender


# Shared properties
class OrderTypeBase(BaseModel):
    nameRu: str
    nameKz: str


# Properties to receive on item creation
class OrderTypeCreate(OrderTypeBase):
    pass


# Properties to receive on item update
class OrderTypeUpdate(OrderTypeBase):
    pass


# Properties shared by models stored in DB
class OrderTypeInDBBase(OrderTypeBase):
    id: int
    nameRu: str
    nameKz: str

    class Config:
        orm_mode = True


# Properties to return to client
class OrderType(OrderTypeBase):
    id: int

    class Config:
        orm_mode = True


# Properties properties stored in DB
class OrderTypeInDB(OrderTypeInDBBase):
    pass

