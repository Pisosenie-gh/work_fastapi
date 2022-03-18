from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.staff_unit_type import StaffUnitType
from app.schemas.staff_unit_type import StaffUnitTypeCreate, StaffUnitTypeUpdate


class CRUDStaffUnitType(CRUDBase[StaffUnitType, StaffUnitTypeCreate, StaffUnitTypeUpdate]):
    def create(
        self, db: Session, *, obj_in: StaffUnitTypeCreate
    ) -> StaffUnitType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[StaffUnitType]:
        return (
            db.query(self.model)
            .filter(StaffUnitType.id == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

staff_unit_type = CRUDStaffUnitType(StaffUnitType)


