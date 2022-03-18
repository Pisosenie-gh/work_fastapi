from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Position])
def read_position(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника должностей
    """

    item = crud.position.get_multi(db, skip=skip, limit=limit)


    return item



@router.post("/", response_model=schemas.Position)
def create_position(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.PositionCreate,

) -> Any:
    """
    Добавление записи справочника должностей
    """
    item = crud.position.create(db=db, obj_in=grade_in)
    return item


@router.put("/{id}", response_model=schemas.Position)
def update_position(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.PositionUpdate,
) -> Any:
    """
    Обновление записи справочника должностей
    """
    item = crud.position.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.position.update(db=db, db_obj=item, obj_in=grade_in)
    return item


@router.get("/{id}", response_model=schemas.Position)
def read_position(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника должностей по id
    """
    item = crud.position.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

