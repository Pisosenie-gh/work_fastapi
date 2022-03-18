from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.NationalityGender])
def read_nationality_gender(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей родов национальности
    """

    item = crud.nationality_gender.get_multi(db, skip=skip, limit=limit)


    return item


@router.post("/", response_model=schemas.NationalityGender)
def create_nationality_gender(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.NationalityGenderCreate,

) -> Any:
    """
    Добавление записи родов национальности
    """
    item = crud.nationality_gender.create(db=db, obj_in=item_in)
    return item


@router.put("/{id}", response_model=schemas.NationalityGender)
def update_nationality_gender(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.NationalityGenderUpdate,
) -> Any:
    """
    Обновление записи родов национальности
    """
    item = crud.nationality_gender.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.nationality_gender.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{id}", response_model=schemas.NationalityGender)
def read_nationality_gender(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись родов национальности по id
    """
    item = crud.nationality_gender.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

