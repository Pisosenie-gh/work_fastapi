
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base




class EmployeeStatus(Base):
    __tablename__ = 'employee_status'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)
