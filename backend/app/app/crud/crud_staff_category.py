from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.staff_category import StaffCategory
from app.schemas.staff_category import StaffCategoryCreate, StaffCategoryUpdate


class CRUDStaffCategory(CRUDBase[StaffCategory, StaffCategoryCreate, StaffCategoryUpdate]):
    def create(
        self, db: Session, *, obj_in: StaffCategoryCreate
    ) -> StaffCategory:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[StaffCategory]:
        return (
            db.query(self.model)
            .filter(StaffCategory.id == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

staff_category = CRUDStaffCategory(StaffCategory)


