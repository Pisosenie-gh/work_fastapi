from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.StaffCategory])
def read_staff_category(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника статусов сотрудника
    """

    item = crud.staff_category.get_multi(db, skip=skip, limit=limit)


    return item



@router.post("/", response_model=schemas.StaffCategory)
def create_staff_category(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.StaffCategoryCreate,

) -> Any:
    """
    Добавление записи справочника статусов сотрудника
    """
    item = crud.staff_category.create(db=db, obj_in=grade_in)
    return item


@router.put("/{id}", response_model=schemas.StaffCategory)
def update_staff_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.StaffCategoryUpdate,
) -> Any:
    """
    Обновление записи справочника статусов сотрудника
    """
    item = crud.staff_category.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.staff_category.update(db=db, db_obj=item, obj_in=grade_in)
    return item


@router.get("/{id}", response_model=schemas.StaffCategory)
def read_staff_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника статуса сотрудника
    """
    item = crud.staff_category.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

