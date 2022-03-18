

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class StaffCategory(Base):
    __tablename__ = 'staff_category'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)



