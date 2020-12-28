from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
# schemas里定义的是响应类,Openapi的响应体格式


class UserBase(BaseModel):
    name: str
    phone: str
    is_active: bool = True
    is_delete: Optional[bool] = False
    education: Optional[int] = None


class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class DepartmentBase(BaseModel):
    name: str


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(DepartmentBase):
    id: int


class DepartmentSchemas(DepartmentBase):
    id: int
    users: List[User]

    class Config:
        orm_mode = True
