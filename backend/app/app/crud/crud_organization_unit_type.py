from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.organization_unit_type import OrganizationUnitType
from app.schemas.organization_unit_type import OrganizationUnitTypeCreate, OrganizationUnitTypeUpdate


class CRUDOrganizationUnitType(CRUDBase[OrganizationUnitType, OrganizationUnitTypeCreate, OrganizationUnitTypeUpdate]):
    def create(
        self, db: Session, *, obj_in: OrganizationUnitTypeCreate
    ) -> OrganizationUnitType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[OrganizationUnitType]:
        return (
            db.query(self.model)
            .filter(OrganizationUnitType.id == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

organization_unit_type = CRUDOrganizationUnitType(OrganizationUnitType)


