from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.nationality import Nationality
from app.schemas.nationality import NationalityCreate,NationalityUpdate


class CRUDNationality(CRUDBase[Nationality, NationalityCreate, NationalityUpdate]):
    def create(
        self, db: Session, *, obj_in: NationalityCreate
    ) -> Nationality:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[Nationality]:
        return (
            db.query(self.model)
            .filter(Nationality.id == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

nationality = CRUDNationality(Nationality)


