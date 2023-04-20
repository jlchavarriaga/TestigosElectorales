from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from apps.api.routers import get_db
from sqlalchemy.orm import Session
from apps.common.querysets.user_queryset import UserQuerySet, User
from apps.common.utils.token import create_access_token, create_refresh_token
from apps.common.utils.password import match_password

router = APIRouter(
    tags=['auth'],
)


@router.post('/login')
def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = UserQuerySet(db).where(User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    if not match_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
    }
