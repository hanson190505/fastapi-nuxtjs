from app.db.base_class import Base
from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime
# 定义映射数据库表的结构

class UserModel(Base):
    __name__ = 'users'
    name = Column(String(30), nullable=False, index=True)
    phone = Column(String(20), nullable=False, index=True, unique=True)
    hashed_password = Column(String(512), nullable=False)
    login_date = Column(DateTime(timezone=True), default=datetime.now)
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)
