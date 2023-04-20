from config import Session
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from apps.common.utils.token import (
    JWT_ALGORITHM,
    JWT_SECRET_KEY
)
from jose import jwt
from pydantic import ValidationError
from apps.common.schemas import TokenPayload
from apps.common.querysets.user_queryset import UserQuerySet, User


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


def get_current_user(token: str = Depends(reuseable_oauth), db=Depends(get_db)) -> User:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = UserQuerySet(db)\
        .where(User.email == token_data.sub)\
        .first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not validated.",
        )

    return user
