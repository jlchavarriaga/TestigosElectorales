from datetime import datetime, timedelta
from jose import jwt
from itsdangerous import URLSafeTimedSerializer
from config.environment import (
    SECRET_KEY,
    EMAIL_SALT_KEY,
    EMAIL_TOKEN_EXPIRE_SECONDS,
    JWT_SECRET_KEY,
    JWT_REFRESH_SECRET_KEY,
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES,
    JWT_ALGORITHM
)


def create_access_token(subject: str, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": subject}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: str, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=JWT_REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": subject}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, JWT_ALGORITHM)
    return encoded_jwt


def generate_email_token(email):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(email, salt=EMAIL_SALT_KEY)


def validate_email_token(token, expiration=EMAIL_TOKEN_EXPIRE_SECONDS):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.loads(token, salt=EMAIL_SALT_KEY, max_age=expiration)
