from config import Session
from apps.common.querysets.user_queryset import UserQuerySet
from apps.common.utils.localize import local_now
from apps.common.validators import AdminUserValidator
from apps.common.commands.tasks.exceptions import InvalidUser
from apps.common.utils.password import get_hashed_password
from apps.common.models.users import User


def create_admin_user(**kwargs):

    au = AdminUserValidator(**kwargs, is_active=True, is_admin=True)

    with Session() as db:
        queryset = UserQuerySet(db)
        if not queryset.where(User.email == kwargs['email']).first():
            u = User()
            for k, v in au.dict().items():
                if k == 'password':
                    setattr(u, k, get_hashed_password(v))
                else:
                    setattr(u, k, v)
            u.created_at = local_now()
            u.updated_at = local_now()

            db.add(u)
            db.commit()
        else:
            raise InvalidUser()
