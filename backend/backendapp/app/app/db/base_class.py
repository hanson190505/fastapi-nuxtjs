
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: int = Column(Integer, primary_key=True, nullable=True, index=True)

    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
