from app.crud.base import CRUDBase
from app.schemas import CategoryCreate, CategoryUpdate, SubCategoryCreate, SubCategoryUpdate
from app.models.model_product import Category, Product, SubCategory


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    pass


class CRUDSubCategory(CRUDBase[SubCategory, SubCategoryCreate, SubCategoryUpdate]):
    pass


category = CRUDCategory(Category)
subcategory = CRUDSubCategory(SubCategory)