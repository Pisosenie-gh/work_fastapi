from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.NationalitySap])
def read_nationality_sap(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника национальности SAP
    """

    item = crud.nationality_sap.get_multi(db, skip=skip, limit=limit)


    return item


@router.post("/", response_model=schemas.NationalitySap)
def create_nationality_sap(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.NationalitySapCreate,

) -> Any:
    """
    Добавление записи справочника национальности SAP
    """
    item = crud.nationality_sap.create(db=db, obj_in=item_in)
    return item


@router.put("/{id}", response_model=schemas.NationalitySap)
def update_nationality_sap(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.NationalitySapUpdate,
) -> Any:
    """
    Обновление записи справочника национальности SAP
    """
    item = crud.nationality_sap.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.nationality_sap.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{id}", response_model=schemas.NationalitySap)
def read_nationality_sap(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника национальности SAP по id
    """
    item = crud.nationality_sap.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

