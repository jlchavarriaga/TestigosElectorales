from apps.common.models.base_model import Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Table, Column, Integer

association_table = Table(
    'orders_products',
    Base.metadata,
    Column('order_id', Integer(), ForeignKey('orders.id')),
    Column('product_id', Integer(), ForeignKey('products.id'))
)
