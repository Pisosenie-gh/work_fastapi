from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.MilitaryServiceAttitude])
def read_military_service_attitude(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей отношений к воинской службе
    """

    item = crud.military_service_attitude.get_multi(db, skip=skip, limit=limit)


    return item



@router.post("/", response_model=schemas.MilitaryServiceAttitude)
def create_military_service_attitude(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.MilitaryServiceAttitudeCreate,

) -> Any:
    """
    Добавление записи отношений к воинской службе
    """
    item = crud.military_service_attitude.create(db=db, obj_in=grade_in)
    return item


@router.put("/{id}", response_model=schemas.MilitaryServiceAttitude)
def update_military_service_attitude(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.MilitaryServiceAttitudeUpdate,
) -> Any:
    """
    Обновление записи отношений к воинской службе
    """
    item = crud.military_service_attitude.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.military_service_attitude.update(db=db, db_obj=item, obj_in=grade_in)
    return item


@router.get("/{id}", response_model=schemas.MilitaryServiceAttitude)
def read_military_service_attitude(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись отношений к воинской службе по id
    """
    item = crud.military_service_attitude.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

