
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from .declination import Declination


class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True, index=True)
    govPositionId = Column(Integer)
    nameRu = Column(String)
    nameKz = Column(String)
    declination_id = Column(Integer, ForeignKey('declination.id'), nullable=True)
    declination = relationship("Declination", backref="position")
