from typing import Any, List

from app.api import deps
from fastapi import APIRouter, Depends
from app.schemas import CategoryCreate, CategoryList, CategoryListBase1
from app.crud import category
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/category')
def create_category(*, db: Session = Depends(deps.get_db), obj_in: CategoryCreate) -> Any:
    category_obj = category.create(db, obj_in=obj_in)
    return category_obj


@router.get('/category/{id}', response_model=CategoryListBase1)
def get_category(*, db: Session = Depends(deps.get_db), id: int):
    category_obj = category.get(db, id=id)
    if category_obj.parent_category > 0:
        pass
    return category_obj


@router.get('/categories', response_model=List[CategoryList])
def get_categories(*, db: Session = Depends(deps.get_db), skip: int, limit: int) -> Any:
    # categories = category.get_category_list(db, skip=skip, limit=limit)
    categories = category.get_multi(db, skip=skip, limit=limit)
    response_categories = []
    for i in categories:
        if i.parent_category == 0:
            response_categories.append(i)
    # return categories
    return response_categories
