from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.OrderChangeType])
def read_order_change_type(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника типов изменения приказа
    """

    item = crud.order_change_type.get_multi(db, skip=skip, limit=limit)


    return item



@router.post("/", response_model=schemas.OrderChangeType)
def create_order_change_type(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.OrderChangeTypeCreate,

) -> Any:
    """
    Добавление записи справочника типов изменения приказа
    """
    item = crud.order_change_type.create(db=db, obj_in=grade_in)
    return item


@router.put("/{id}", response_model=schemas.OrderChangeType)
def update_order_change_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.OrderChangeTypeUpdate,
) -> Any:
    """
    Обновление записи справочника типов изменения приказа
    """
    item = crud.order_change_type.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.order_change_type.update(db=db, db_obj=item, obj_in=grade_in)
    return item


@router.get("/{id}", response_model=schemas.OrderChangeType)
def read_order_change_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника типов изменения приказа по id
    """
    item = crud.order_change_type.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

