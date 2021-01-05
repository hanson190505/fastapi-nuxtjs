from typing import Optional, List, Union, Dict
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    parent_category: int


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryListBase2(BaseModel):
    id: int
    name: str
    parent_category: int
    sub_categories: List

    class Config:
        orm_mode = True


class CategoryListBase1(BaseModel):
    id: int
    name: str
    parent_category: int
    sub_categories: List[CategoryListBase2]

    class Config:
        orm_mode = True


class CategoryListBase(BaseModel):
    id: int
    name: str
    parent_category: int
    sub_categories: List[CategoryListBase1]

    class Config:
        orm_mode = True


class CategoryList(BaseModel):
    id: int
    name: str
    parent_category: int
    sub_categories: List[CategoryListBase]

    class Config:
        orm_mode = True


CategoryList.update_forward_refs()


class ProductBase(BaseModel):
    pass


