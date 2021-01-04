from app.db.base_class import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref


class Category(Base):
    name = Column(String(64), unique=True, index=True)
    parent_category = Column(Integer, ForeignKey('category.id'), nullable=True)
    sub_categories = relationship('Category')


class Product(Base):
    number = Column(String(128), unique=True, index=True)
    name = Column(String(128), index=True)
    seo_title = Column(String(256), nullable=True)
    seo_description = Column(String(1024), nullable=True)
    material = Column(String(128), default='custom')
    color = Column(String(128), nullable=True)