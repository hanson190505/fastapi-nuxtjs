from app.core.security import get_password_hash
from app.crud.base import CRUDBase
from app.models.user import UserModel
from app.schemas.user import UserCreate, UserUpdate
from sqlalchemy.orm import Session
# 控制器


class CRUDUser(CRUDBase[UserModel, UserCreate, UserUpdate]):

    def create(self, db: Session, *, obj_in: UserCreate) -> UserModel:
        db_obj = UserModel(
            name=obj_in.name,
            phone=obj_in.phone,
            hashed_password=get_password_hash(obj_in.password)
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


user = CRUDUser(UserModel)