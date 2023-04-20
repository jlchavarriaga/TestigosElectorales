from apps.common.models.base_model import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy_serializer import SerializerMixin


class Product(Base, SerializerMixin):

    __tablename__ = 'products'

    serialize_only = (
        'id',
        'name',
        'description',
        'price',
        'created_at',
        'updated_at'
    )

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
