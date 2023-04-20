from apps.common.querysets.base_queryset import BaseQuerySet
from apps.common.models.orders import Order
from sqlalchemy.orm import Session


class OrderQuerySet(BaseQuerySet):
    def __init__(self, db: Session) -> None:
        super().__init__(Order, db)
