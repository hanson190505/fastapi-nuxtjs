from typing import Union, Dict, Any, Optional

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase, UpdateSchemaType
from app.models.user import UserModel
from app.schemas.user import UserCreate, UserUpdate, User
from sqlalchemy.orm import Session


# 控制器


class CRUDUser(CRUDBase[UserModel, UserCreate, UserUpdate]):
    
    def get_by_phone(self, db: Session, *, phone: str) -> UserModel:
        return db.query(UserModel).filter(phone == phone).first()

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

    def update(self, db: Session, *, db_obj: UserModel, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> User:
        if isinstance(db_obj, Dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data['password']:
            hash_password = get_password_hash(update_data['password'])
            del update_data['password']
            update_data['hash_password'] = hash_password
        return super(CRUDUser, self).update(db, db_obj=db_obj, obj_in=update_data)
    
    def authenticate(self, db: Session, *, phone: str, password: str) -> Optional[UserModel]:
        user = self.get_by_phone(db, phone=phone)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(UserModel)
