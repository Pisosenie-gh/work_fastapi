from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Nationality])
def read_nationality(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника национальности
    """

    item = crud.nationality.get_multi(db, skip=skip, limit=limit)


    return item


@router.post("/", response_model=schemas.Nationality)
def create_nationality(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.NationalityCreate,

) -> Any:
    """
    Добавление записи справочника национальности
    """
    item = crud.nationality.create(db=db, obj_in=item_in)
    return item


@router.put("/{id}", response_model=schemas.Nationality)
def update_nationality(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.NationalityUpdate,
) -> Any:
    """
    Обновление записи справочника национальности
    """
    item = crud.nationality.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.nationality.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{id}", response_model=schemas.Nationality)
def read_nationality(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника национальности
    """
    item = crud.nationality.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

