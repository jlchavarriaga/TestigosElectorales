from sqlalchemy import create_engine as create
from sqlalchemy.orm import sessionmaker
import config.environment as env


def create_engine():
    return create(env.POSTGRES['URI'])


def create_test_engine():
    return create(env.DEVELOPMENT['POSTGRES_URI_TEST'])


class Postgres:
    @staticmethod
    def create_session_factory():
        # Testing approach for isolation of testing scripts
        if env.ENVIRONMENT['APP_ENV'] in ['testing']:
            engine = create_test_engine()
        else:
            engine = create_engine()
        return sessionmaker(bind=engine)
