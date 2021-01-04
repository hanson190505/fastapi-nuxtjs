from typing import Optional, List
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    parent_category: int


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryInDBBase(CategoryBase):
    id: int
    sub_categories: List[CategoryBase]

    class Config:
        orm_mode = True


class Category(CategoryInDBBase):
    pass

