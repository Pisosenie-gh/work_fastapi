from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.military_service_attitude import MilitaryServiceAttitude
from app.schemas.military_service_attitude import MilitaryServiceAttitudeCreate, MilitaryServiceAttitudeUpdate


class CRUDMilitaryServiceAttitude(CRUDBase[MilitaryServiceAttitude, MilitaryServiceAttitudeCreate, MilitaryServiceAttitudeUpdate]):
    def create(
        self, db: Session, *, obj_in: MilitaryServiceAttitudeCreate
    ) -> MilitaryServiceAttitude:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[MilitaryServiceAttitude]:
        return (
            db.query(self.model)
            .filter(MilitaryServiceAttitude.id == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

military_service_attitude = CRUDMilitaryServiceAttitude(MilitaryServiceAttitude)


