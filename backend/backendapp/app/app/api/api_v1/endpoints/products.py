from typing import Any

from app.api import deps
from fastapi import APIRouter, Depends
from app.schemas import CategoryCreate, SubCategoryCreate, Category
from app.crud import category, subcategory
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/category')
def create_category(*, db: Session = Depends(deps.get_db), obj_in: CategoryCreate) -> Any:
    category_obj = category.create(db, obj_in=obj_in)
    return category_obj


@router.get('/category/{id}', response_model=Category)
def get_category(*, db: Session = Depends(deps.get_db), id: int):
    category_obj = category.get(db, id=id)
    return category_obj


@router.post('/subcategory')
def create_subcategory(*, db: Session = Depends(deps.get_db), obj_in: SubCategoryCreate) -> Any:
    subcategory_obj = subcategory.create(db, obj_in=obj_in)
    return subcategory_obj
