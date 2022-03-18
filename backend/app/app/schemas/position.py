from typing import Optional, List

from pydantic import BaseModel, Field
from datetime import date

from .declination import Declination, DeclinationForModels


# Shared properties
class PositionBase(BaseModel):
    govPositionId: int
    nameRu: str
    nameKz: str
    declination: Declination

# Properties to receive on item creation
class PositionCreate(PositionBase):
    declination: Optional[DeclinationForModels] =None

class PositionCreateIn(PositionBase):
    declination: Optional[Declination] = None


# Properties to receive on item update
class PositionUpdate(PositionBase):
    declination: Declination

# Properties shared by models stored in DB
class PositionInDBBase(PositionBase):
    id: int
    govPositionId: int
    nameRu: str
    nameKz: str
    declination: Declination

    class Config:
        orm_mode = True


# Properties to return to client
class Position(PositionBase):
    id: int
    govPositionId: int
    nameRu: str
    nameKz: str
    declination: Declination

    class Config:
        orm_mode = True


# Properties properties stored in DB
class PositionInDB(PositionInDBBase):
    pass

