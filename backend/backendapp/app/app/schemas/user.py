from typing import Optional
from datetime import datetime
from pydantic import BaseModel
# schemas里定义的是响应类,Openapi的响应体格式


# Shared properties
class UserBase(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = True


# Properties to receive via API on creation
class UserCreate(UserBase):
    name: str
    phone: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    is_delete: bool
    phone: str
    education: int


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
