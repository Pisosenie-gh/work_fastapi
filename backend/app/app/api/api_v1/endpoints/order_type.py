from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.OrderType])
def read_order_type(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника типов приказа
    """

    item = crud.order_type.get_multi(db, skip=skip, limit=limit)


    return item



@router.post("/", response_model=schemas.OrderType)
def create_order_type(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.OrderTypeCreate,

) -> Any:
    """
    Добавление записи справочника типов приказа
    """
    item = crud.order_type.create(db=db, obj_in=grade_in)
    return item


@router.put("/{id}", response_model=schemas.OrderType)
def update_order_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.OrderTypeUpdate,
) -> Any:
    """
    Обновление записи справочника типов приказа
    """
    item = crud.order_type.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.order_type.update(db=db, db_obj=item, obj_in=grade_in)
    return item


@router.get("/{id}", response_model=schemas.OrderType)
def read_order_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника Тип приказа по id
    """
    item = crud.order_type.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

