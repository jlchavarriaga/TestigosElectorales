from apps.common.handlers.base_handler import BaseHandler, run
from apps.common.querysets.order_queryset import OrderQuerySet
from apps.common.querysets.product_queryset import ProductQuerySet
from apps.common.utils.localize import local_now
from apps.common.validators import OrderValidator
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


class OrderHandler(BaseHandler):
    queryset_class = OrderQuerySet

    @classmethod
    def get_existent_products(cls, db: Session, order: OrderValidator):
        queryset = ProductQuerySet(db)

        products = queryset\
            .where(queryset.model.id.in_([p.id for p in order.products]))\
            .where(queryset.model.deleted_at == None)\
            .all()

        if products:
            return products
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Invalid products.'
            )

    @classmethod
    @run
    def create_item(cls, db: Session, order: OrderValidator):
        queryset = cls.queryset_class(db)

        products = cls.get_existent_products(db, order)

        record = queryset.model(
            name=order.name,
            description=order.description,
            created_at=local_now(),
            updated_at=local_now()
        )

        for p in products:
            record.products.append(p)

        queryset.create(record)

        return record.to_dict()

    @classmethod
    @run
    def update_item(cls, db: Session, id: int, order: OrderValidator):
        queryset = cls.queryset_class(db)

        record = queryset.find(id)

        if record:
            record.name = order.name
            record.description = order.description
            # Clear all current products in order
            record.products.clear()

            products = cls.get_existent_products(db, order)

            for p in products:
                record.products.append(p)

            record.updated_at = local_now()
            queryset.db.commit()

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Record does not exist.'
            )

        return record.to_dict()
