from typing import Optional

from pydantic import BaseModel
from datetime import date

# Shared properties
class DeclinationBase(BaseModel):
    ruIP: str
    ruRP: str
    ruDP: str
    ruTP: str
    ruVP: str
    ruPP: str
    kzAS: str
    kzIS: str
    kzBS: str
    kzZS: str
    kzTS: str
    kzSS: str
    kzKS: str



# Properties to receive on item creation
class DeclinationCreate(DeclinationBase):
    pass


# Properties to receive on item update
class DeclinationUpdate(DeclinationBase):
    pass


class DeclinationForModels(BaseModel):
    ruIP: str
    ruRP: str
    ruDP: str
    ruTP: str
    ruVP: str
    ruPP: str
    kzAS: str
    kzIS: str
    kzBS: str
    kzZS: str
    kzTS: str
    kzSS: str
    kzKS: str
    class Config:
        orm_mode = True


# Properties shared by models stored in DB
class DeclinationInDBBase(DeclinationBase):
    id: int
    ruIP: str
    ruRP: str
    ruDP: str
    ruTP: str
    ruVP: str
    ruPP: str
    kzAS: str
    kzIS: str
    kzBS: str
    kzZS: str
    kzTS: str
    kzSS: str
    kzKS: str


    class Config:
        orm_mode = True


# Properties to return to client
class Declination(DeclinationInDBBase):
    id: int
    ruIP: str
    ruRP: str
    ruDP: str
    ruTP: str
    ruVP: str
    ruPP: str
    kzAS: str
    kzIS: str
    kzBS: str
    kzZS: str
    kzTS: str
    kzSS: str
    kzKS: str


# Properties properties stored in DB
class DeclinationInDB(DeclinationInDBBase):
    pass

