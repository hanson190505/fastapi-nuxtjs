from typing import Optional, List

from pydantic import BaseModel


class SubCategoryBase(BaseModel):
    name: str
    category_id: int


class SubCategoryCreate(SubCategoryBase):
    pass


class SubCategoryUpdate(SubCategoryBase):
    pass


class SubCategoryInDBBase(SubCategoryBase):
    class Config:
        orm_mode = True


class SubCategory(SubCategoryInDBBase):
    pass


class CategoryBase(BaseModel):
    name: Optional[str] = None


class CategoryCreate(CategoryBase):
    name: str


class CategoryUpdate(CategoryBase):
    pass


class CategoryInDBBase(CategoryBase):
    id: int
    name: str
    sub_category: List[SubCategory]

    class Config:
        orm_mode = True


class Category(CategoryInDBBase):
    pass


