from pydantic import BaseModel, Extra, validator
from typing import Optional


class UserValidator(BaseModel, extra=Extra.forbid):
    username: str
    email: str
    password: str

    @validator('email')
    def valid_email(cls, v):
        if not ('@' in v and v.endswith('.com')):
            raise ValueError('Invalid email')
        return v


class AdminUserValidator(UserValidator):
    is_admin: Optional[bool] = False
    is_active: Optional[bool] = False


class ProductValidator(BaseModel, extra=Extra.forbid):
    name: str
    description: str
    price: float


class IdProductValidator(BaseModel, extra=Extra.forbid):
    id: int


class OrderValidator(BaseModel, extra=Extra.forbid):
    name: str
    description: str
    products: list[IdProductValidator]
