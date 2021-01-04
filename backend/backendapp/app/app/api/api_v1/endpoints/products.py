from typing import Any, List

from app.api import deps
from fastapi import APIRouter, Depends
from app.schemas import CategoryCreate, Category
from app.crud import category
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/category')
def create_category(*, db: Session = Depends(deps.get_db), obj_in: CategoryCreate) -> Any:
    category_obj = category.create(db, obj_in=obj_in)
    return category_obj


@router.get('/category/{id}')
def get_category(*, db: Session = Depends(deps.get_db), id: int):
    category_obj = category.get(db, id=id)
    if category_obj.parent_category > 0:
        pass
    return category_obj


@router.get('/category')
def get_categories(*, db: Session = Depends(deps.get_db), skip: int, limit: int) -> Any:
    categories = category.get_multi(db, skip=skip, limit=limit)
    return categories
