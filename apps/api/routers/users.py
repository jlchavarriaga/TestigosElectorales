from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from apps.api.routers import get_db, get_current_user
from apps.common.validators import UserValidator, AdminUserValidator
from apps.api.api_responser import ApiResponser
from apps.common.querysets.user_queryset import User
from apps.common.handlers.registration_handler import RegistrationHandler
from apps.common.handlers.user_handler import UserHandler

router = APIRouter(
    prefix='/api/v1',
    tags=['users']
)


@router.get('/users')
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.is_admin:
        return UserHandler.get_items(db)
    else:
        return ApiResponser.unauthorized_response('Current user does not have access to this content.')


@router.post('/users')
def create_user(
    user: AdminUserValidator,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    print(user)
    if current_user.is_admin:
        return UserHandler.create_item(db, user)
    else:
        return ApiResponser.unauthorized_response("Current user can't create users.")


@router.put('/users/{email}')
def update_user(
    email,
    user: AdminUserValidator,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.is_admin:
        return UserHandler.update_item(db, email, user)
    else:
        return ApiResponser.unauthorized_response("Current user can't update users.")


@router.delete('/users/{email}')
def delete_user(
    email,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.is_admin:
        return UserHandler.delete_item(db, email)
    else:
        return ApiResponser.unauthorized_response("Current user can't delete users.")


@router.post('/users/registration')
def register_user(
    user: UserValidator,
    db: Session = Depends(get_db)
):
    return RegistrationHandler.register(db, user)


@router.get('/users/confirm/{token}')
def confirm_user(
    token,
    db: Session = Depends(get_db)
):
    return RegistrationHandler.validate(db, token)


@router.get('/users/me')
def me(
    current_user: User = Depends(get_current_user)
):
    return ApiResponser.success_response({'user': current_user.email, 'alias': current_user.username})
