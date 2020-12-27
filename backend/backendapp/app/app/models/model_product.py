from app.db.base_class import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Category(Base):
    name: str = Column(String(64), unique=True, index=True)

    sub_category = relationship('SubCategory', back_populates='parent_category')


class SubCategory(Base):
    name = Column(String(64), unique=True, index=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    parent_category = relationship('Category', back_populates='sub_category')
    products = relationship('Product', back_populates='category')


class Product(Base):
    number = Column(String(128), unique=True, index=True)
    name = Column(String(128), index=True)
    seo_title = Column(String(256), nullable=True)
    seo_description = Column(String(1024), nullable=True)
    material = Column(String(128), default='custom')
    color = Column(String(128), nullable=True)

    sub_category_id = Column(Integer, ForeignKey('subcategory.id'))
    category = relationship('SubCategory', back_populates='products')