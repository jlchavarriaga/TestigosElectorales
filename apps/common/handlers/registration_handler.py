from apps.common.utils.tasks import enqueue_task
from apps.api.api_responser import ApiResponser
from apps.common.validators import UserValidator
from apps.common.querysets.user_queryset import UserQuerySet, User
from apps.common.utils.password import get_hashed_password
from apps.common.utils.token import generate_email_token, validate_email_token
from itsdangerous import SignatureExpired, BadSignature
from apps.common.utils.localize import local_now
from config.environment import BASE_URL


def run(f):
    def wrapper(*args, **kwargs):
        try:
            output = f(*args, **kwargs)
        except SignatureExpired:
            return ApiResponser.bad_request_response('Confirmation token has expired.')
        except BadSignature:
            return ApiResponser.bad_request_response('Token is invalid')
        except Exception as e:
            return ApiResponser.error_response(e)
        return output
    return wrapper


class RegistrationHandler:
    @staticmethod
    @run
    def register(db, user: UserValidator):
        queryset = UserQuerySet(db)

        if queryset.where(User.email == user.email).first():
            return ApiResponser.bad_request_response(f'An user with email {user.email} already exists.')
        else:
            u = User()
            for k, v in user.dict().items():
                if k == 'password':
                    setattr(u, k, get_hashed_password(v))
                else:
                    setattr(u, k, v)

            u.created_at = local_now()
            u.updated_at = local_now()

            queryset.create(u)

            token = generate_email_token(user.email)
            body = "User validation email.\n To enable your account" \
                "please use the following link:\n" \
                f"{BASE_URL}/api/v1/users/confirm/{token}"

            enqueue_task('validation_email', user.email,
                         subject="User activation", body=body)

        return ApiResponser.success_response(user.json())

    @staticmethod
    @run
    def validate(db, token):
        queryset = UserQuerySet(db)

        email = validate_email_token(token)
        user = queryset\
            .where(User.email == email)\
            .first()

        queryset.enable_user(user)

        print(f'User {user.email} is active now.')

        return ApiResponser.success_response({"message": f"User {user.email} has been validated successfully."})
