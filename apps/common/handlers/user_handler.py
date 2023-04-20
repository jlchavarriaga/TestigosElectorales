from apps.common.handlers.base_handler import BaseHandler, run
from apps.common.querysets.user_queryset import UserQuerySet
from apps.common.utils.localize import local_now
from fastapi import HTTPException, status
from apps.common.utils.password import get_hashed_password
from apps.common.validators import AdminUserValidator
from sqlalchemy.orm import Session


class UserHandler(BaseHandler):
    queryset_class = UserQuerySet

    @classmethod
    @run
    def create_item(cls, db: Session, user: AdminUserValidator):
        queryset = cls.queryset_class(db)

        if not queryset.where(queryset.model.email == user.email).first():
            record = queryset.model()
            for k, v in user.dict().items():
                if k == 'password':
                    setattr(record, k, get_hashed_password(v))
                else:
                    setattr(record, k, v)

            record.created_at = local_now()
            record.updated_at = local_now()

            queryset.create(record)

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'An user with email {user.email} already exists.'
            )

        return user

    @classmethod
    @run
    def update_item(cls, db: Session, email: str, user: AdminUserValidator):
        queryset = cls.queryset_class(db)

        if not queryset.where(queryset.model.email == user.email).first():
            record = queryset.where(queryset.model.email == email)\
                .first()

            if record:
                for k, v in user.dict().items():
                    if k == 'password':
                        setattr(record, k, get_hashed_password(v))
                    else:
                        setattr(record, k, v)

                record.updated_at = local_now()

                queryset.db.commit()
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Record does not exist.'
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'An user with email {user.email} already exists.'
            )

        return user

    @classmethod
    @run
    def delete_item(cls, db: Session, email: str):

        queryset = cls.queryset_class(db)

        record = queryset.where(queryset.model.email == email)\
            .first()

        if record:
            record.deleted_at = local_now()
            record.is_active = False
            queryset.db.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Record does not exist.'
            )

        return {'detail': 'OK'}
