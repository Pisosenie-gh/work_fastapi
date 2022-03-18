from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.OrganizationUnitType])
def read_organization_unit_type(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника типов структурной единицы
    """

    item = crud.organization_unit_type.get_multi(db, skip=skip, limit=limit)


    return item



@router.post("/", response_model=schemas.OrganizationUnitType)
def create_organization_unit_type(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.OrganizationUnitTypeCreate,

) -> Any:
    """
    Добавление записи справочника типов структурной единицы
    """
    item = crud.organization_unit_type.create(db=db, obj_in=grade_in)
    return item


@router.put("/{id}", response_model=schemas.OrganizationUnitType)
def update_organization_unit_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.OrganizationUnitTypeUpdate,
) -> Any:
    """
    Обновление записи справочника типов структурной единицы
    """
    item = crud.organization_unit_type.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.organization_unit_type.update(db=db, db_obj=item, obj_in=grade_in)
    return item


@router.get("/{id}", response_model=schemas.OrganizationUnitType)
def read_organization_unit_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника типов структурной единицы по id
    """
    item = crud.organization_unit_type.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

