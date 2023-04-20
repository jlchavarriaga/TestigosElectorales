from apps.common.querysets.base_queryset import BaseQuerySet
from apps.common.models.products import Product
from sqlalchemy.orm import Session


class ProductQuerySet(BaseQuerySet):
    def __init__(self, db: Session) -> None:
        super().__init__(Product, db)
