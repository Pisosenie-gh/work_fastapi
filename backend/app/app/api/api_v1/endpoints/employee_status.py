from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.EmployeeStatus])
def read_employee_status(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника статусов сотрудника
    """

    item = crud.employee_status.get_multi(db, skip=skip, limit=limit)


    return item



@router.post("/", response_model=schemas.EmployeeStatus)
def create_employee_status(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.EmployeeStatusCreate,

) -> Any:
    """
    Добавление записи справочника статусов сотрудника
    """
    item = crud.employee_status.create(db=db, obj_in=grade_in)
    return item


@router.put("/{id}", response_model=schemas.EmployeeStatus)
def update_employee_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.EmployeeStatusUpdate,
) -> Any:
    """
    Обновление записи справочника статусов сотрудника
    """
    item = crud.employee_status.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.employee_status.update(db=db, db_obj=item, obj_in=grade_in)
    return item


@router.get("/{id}", response_model=schemas.EmployeeStatus)
def read_employee_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника статуса сотрудника
    """
    item = crud.employee_status.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item

