from app.db.base_class import Base
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from datetime import datetime
# 定义映射数据库表的结构


class DepartmentModel(Base):
    name = Column(String(32), nullable=False, index=True)
    pub_date = Column(DateTime(timezone=True), default=datetime.now)


class UserModel(Base):
    name = Column(String(30), nullable=False, index=True)
    phone = Column(String(20), nullable=False, index=True, unique=True)
    hashed_password = Column(String(512), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=False)
    education = Column(Integer, default=1)
