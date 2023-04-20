from apps.common.utils.localize import local_now
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def run(f):
    def wrapper(*args, **kwargs):
        try:
            output = f(*args, **kwargs)
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error has ocurred, contact system administrator. Detail: {e}"
            )
        return output
    return wrapper


class BaseHandler:

    @classmethod
    @run
    def get_items(cls, db: Session):
        return [
            i.to_dict()
            for i in cls.queryset_class(db).get()
        ]

    @classmethod
    @run
    def create_item(cls, db: Session, item):
        queryset = cls.queryset_class(db)

        record = queryset.model(
            **item.dict(),
            created_at=local_now(),
            updated_at=local_now()
        )

        queryset.create(record)

        return item

    @classmethod
    @run
    def create_items(cls, db: Session, items):
        queryset = cls.queryset_class(db)

        records = [
            queryset.model(
                **i.dict(),
                created_at=local_now(),
                updated_at=local_now()
            )
            for i in items
        ]

        queryset.create_all(records)

        return items

    @classmethod
    @run
    def update_item(cls, db: Session, id: int, item):
        queryset = cls.queryset_class(db)

        record = queryset.find(id)

        if record:
            for k, v in item.dict().items():
                setattr(record, k, v)

            record.updated_at = local_now()

            queryset.db.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Record does not exist.'
            )

        return item

    @classmethod
    @run
    def delete_item(cls, db: Session, id: int):

        queryset = cls.queryset_class(db)

        record = queryset.find(id)
        if record:
            record.deleted_at = local_now()
            queryset.db.commit()
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Record does not exist.'
            )

        return {'detail': 'OK'}
