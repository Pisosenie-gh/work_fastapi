from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.MaritalStatus])
def read_marital_status(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника семейного положения
    """

    item = crud.marital_status.get_multi(db, skip=skip, limit=limit)


    return item



@router.post("/", response_model=schemas.MaritalStatus)
def create_marital_status(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.MaritalStatusCreate,

) -> Any:
    """
    Добавление записи справочника семейного положения
    """
    item = crud.marital_status.create(db=db, obj_in=grade_in)
    return item


@router.put("/{id}", response_model=schemas.MaritalStatus)
def update_marital_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.MaritalStatusUpdate,
) -> Any:
    """
    Обновление записи справочника семейного положения
    """
    item = crud.marital_status.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.marital_status.update(db=db, db_obj=item, obj_in=grade_in)
    return item


@router.get("/{id}", response_model=schemas.MaritalStatus)
def read_marital_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника семейного положения по id
    """
    item = crud.marital_status.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

