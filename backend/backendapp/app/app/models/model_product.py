from app.db.base_class import Base
from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship


class ProductCategoryModel(Base):
    name: str = Column(String(64), unique=True, index=True)

    sub_category = relationship('ProductSubCategoryModel', back_populates='parent_category')


class ProductSubCategoryModel(Base):
    name: str = Column(String(64), unique=True, index=True)
    product_category_id = Column(Integer, ForeignKey('productcategorymodel.id'))
    parent_category = relationship('ProductCategoryModel', back_populates='sub_category')


class ProductModel(Base):
    number: str = Column(String(128), unique=True, index=True)
    name: str = Column(String(128), unique=True, index=True)

    product_sub_category_id = Column(Integer, ForeignKey('productsubcategorymodel.id'))
    category = relationship('ProductSubCategoryModel', back_populates='products')