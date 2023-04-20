from apps.common.models.base_model import Base
from apps.common.models.orders_products import association_table
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin


class Order(Base, SerializerMixin):

    __tablename__ = 'orders'

    serialize_only = (
        'name',
        'description',
        'products',
        'created_at',
        'updated_at'
    )

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    products = relationship("Product", secondary=association_table)
