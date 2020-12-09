from typing import List, Optional

from pydantic import BaseModel


class BooksBase(BaseModel):
    title: str
    description: Optional[str] = None


class BooksCreate(BooksBase):
    pass


class Book(BooksBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    books: List[Book] = []

    class Config:
        orm_mode = True
