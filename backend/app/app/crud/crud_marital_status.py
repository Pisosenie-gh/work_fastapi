from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.marital_status import MaritalStatus
from app.schemas.marital_status import MaritalStatusCreate, MaritalStatusUpdate


class CRUDMaritalStatus(CRUDBase[MaritalStatus, MaritalStatusCreate, MaritalStatusUpdate]):
    def create(
        self, db: Session, *, obj_in: MaritalStatusCreate
    ) -> MaritalStatus:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[MaritalStatus]:
        return (
            db.query(self.model)
            .filter(MaritalStatus.id == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

marital_status = CRUDMaritalStatus(MaritalStatus)


