from datetime import timedelta
from typing import Any

from app import schemas, crud
from app.api import deps
from app.core import security
from app.core.config import settings
from app.schemas.schemas_user import UserLogin
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/login/access_token", response_model=schemas.Token)
def login_access_token(
        *,
        db: Session = Depends(deps.get_db),
        form_data: UserLogin
) -> Any:
    user = crud.user.authenticate(db, phone=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

