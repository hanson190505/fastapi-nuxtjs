from typing import Any, List

from app import schemas, crud
from app.api import deps
from app.schemas import DepartmentSchemas, DepartmentCreate, DepartmentUpdate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/{id}', response_model=DepartmentSchemas)
def get_users_by_department():
    pass


@router.get('/', response_model=List[DepartmentSchemas])
def get_departments(
        db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100,
) -> Any:
    departments = crud.crud_department.get_multi(db, skip=skip, limit=limit)
    return departments


@router.post('/', response_model=DepartmentSchemas)
def create_department(
        *,
        db: Session = Depends(deps.get_db),
        department_in: schemas.DepartmentCreate
) -> Any:
    department = crud.crud_department.create(db, obj_in=department_in)
    return department
