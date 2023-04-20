from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from apps.api.routers import get_db, get_current_user
from apps.common.models.users import User
from apps.common.validators import OrderValidator
from apps.common.handlers.order_handler import OrderHandler

router = APIRouter(
    prefix='/api/v1',
    tags=['orders']
)


@router.get('/orders')
def get_orders(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return OrderHandler.get_items(db)


@router.post('/orders')
def create_order(
    order: OrderValidator,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return OrderHandler.create_item(db, order)


@router.put('/orders/{id}')
def update_order(
    id,
    order: OrderValidator,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return OrderHandler.update_item(db, id, order)


@router.delete('/orders/{id}')
def delete_order(
    id,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return OrderHandler.delete_item(db, id)
