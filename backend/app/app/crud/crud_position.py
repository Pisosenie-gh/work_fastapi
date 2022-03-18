from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.position import Position
from app.schemas.position import PositionCreate, PositionUpdate, PositionCreateIn
from app.models.declination import Declination

class CRUDPosition(CRUDBase[Position, PositionCreateIn, PositionUpdate]):
    def create(
        self, db: Session, *, obj_in: PositionCreateIn
    ) -> Position:

        declination = jsonable_encoder(obj_in.declination)

        db_obj = Position(
            govPositionId=obj_in.govPositionId,
            nameRu=obj_in.nameRu,
            nameKz=obj_in.nameKz,
            declination=Declination(**declination),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_id(
        self, db: Session, *, id: int, skip: int = 0, limit: int = 100
    ) -> List[Position]:
        return (
            db.query(self.model)
            .filter(Position.id == id)
            .offset(skip)
            .limit(limit)
            .all()
        )

position = CRUDPosition(Position)


