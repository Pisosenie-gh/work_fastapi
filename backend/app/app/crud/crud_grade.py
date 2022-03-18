from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.grade import Grade
from app.schemas.grade import GradeCreate, GradeUpdate


class CRUDGrade(CRUDBase[Grade, GradeCreate, GradeUpdate]):
    def create(
        self, db: Session, *, obj_in: GradeCreate
    ) -> Grade:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[Grade]:
        return (
            db.query(self.model)
            .filter(Grade.id == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

grade = CRUDGrade(Grade)


