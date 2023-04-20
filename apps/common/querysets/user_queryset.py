from apps.common.models.users import User
from apps.common.querysets.base_queryset import BaseQuerySet
from sqlalchemy.orm import Session


class UserQuerySet(BaseQuerySet):
    def __init__(self, db: Session) -> None:
        super().__init__(User, db)

    def enable_user(self, user: User):
        user.is_active = True
        self.db.commit()
