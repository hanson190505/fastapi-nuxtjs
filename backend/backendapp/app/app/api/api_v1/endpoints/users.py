from fastapi import APIRouter, Depends
from app import schemas, crud
from typing import List, Any
from app.api import deps
from sqlalchemy.orm import Session
# api接口定义

router = APIRouter()


@router.get('/', response_model=List[schemas.User])
def get_users(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100) -> Any:
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post('/', response_model=schemas.User)
def post_user(*, db: Session = Depends(deps.get_db), user_in: schemas.UserCreate) -> Any:
    user = crud.user.create(db, obj_in=user_in)
    return user
