from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from apps.api.routers import get_db, get_current_user
from apps.common.models.users import User
from apps.common.validators import ProductValidator
from apps.common.handlers.product_handler import ProductHandler

router = APIRouter(
    prefix='/api/v1',
    tags=['products']
)


@router.get('/products')
def get_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ProductHandler.get_items(db)


@router.post('/products')
def create_products(
    products: list[ProductValidator],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ProductHandler.create_items(db, products)


@router.put('/products/{id}')
def update_product(
    id,
    product: ProductValidator,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return ProductHandler.update_item(db, id, product)


@router.delete('/products/{id}')
def delete_product(
    id,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ProductHandler.delete_item(db, id)
