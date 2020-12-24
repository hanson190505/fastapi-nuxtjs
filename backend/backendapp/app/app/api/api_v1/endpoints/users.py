from fastapi import APIRouter, Depends
from app import schemas, crud, models
from typing import List, Any
from app.api import deps
from sqlalchemy.orm import Session

# api接口定义

router = APIRouter()


@router.get('/', response_model=List[schemas.User])
def get_users(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100,
              current_user: models.UserModel = Depends(deps.get_current_active_user)
              ) -> Any:
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post('/', response_model=schemas.User)
def post_user(*, db: Session = Depends(deps.get_db), user_in: schemas.UserCreate) -> Any:
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.patch('/', response_model=schemas.User)
def patch_user(*, db: Session = Depends(deps.get_db), user_in: schemas.UserUpdate) -> Any:
    user = crud.user.update(db, obj_in=user_in)
    return user
