from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.nationality_sap import NationalitySap
from app.schemas.nationality_sap import NationalitySapCreate,NationalitySapUpdate


class CRUDNationalitySap(CRUDBase[NationalitySap, NationalitySapCreate, NationalitySapUpdate]):
    def create(
        self, db: Session, *, obj_in: NationalitySapCreate
    ) -> NationalitySap:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[NationalitySap]:
        return (
            db.query(self.model)
            .filter(NationalitySap.id == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

nationality_sap = CRUDNationalitySap(NationalitySap)


