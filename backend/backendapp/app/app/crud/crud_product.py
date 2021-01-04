from app.crud.base import CRUDBase
from app.schemas import CategoryCreate, CategoryUpdate
from app.models.model_product import Category, Product


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    pass


category = CRUDCategory(Category)