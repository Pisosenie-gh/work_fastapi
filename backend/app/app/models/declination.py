
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Declination(Base):
    __tablename__ = 'declination'

    id = Column(Integer, primary_key=True, index=True)
    ruIP = Column(String)
    ruRP = Column(String,nullable=True)
    ruDP = Column(String,nullable=True)
    ruTP = Column(String,nullable=True)
    ruVP = Column(String,nullable=True)
    ruPP = Column(String,nullable=True)
    kzAS = Column(String,nullable=True)
    kzIS = Column(String,nullable=True)
    kzBS = Column(String,nullable=True)
    kzZS = Column(String,nullable=True)
    kzTS = Column(String,nullable=True)
    kzSS = Column(String,nullable=True)
    kzKS = Column(String,nullable=True)


