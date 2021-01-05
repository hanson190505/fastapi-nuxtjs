from typing import Any

from app.crud.base import CRUDBase
from app.schemas import CategoryCreate, CategoryUpdate
from app.models.model_product import Category, Product
from sqlalchemy.orm import Session


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def get_category_list(self, db: Session, *, skip: int = 0, limit: int = 100) -> Any:
        return db.query(self.model).filter(self.model.parent_category == 0).offset(skip).limit(limit).all()


category = CRUDCategory(Category)