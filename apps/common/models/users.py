from apps.common.models.base_model import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy_serializer import SerializerMixin


class User(Base, SerializerMixin):

    __tablename__ = 'users'

    serialize_only = (
        'id',
        'username',
        'email',
        'created_at',
        'updated_at'
    )

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
