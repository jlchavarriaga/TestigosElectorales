from unittest import TestCase
from os.path import dirname, join
import json
from config.postgres import create_test_engine
from sqlalchemy.orm import sessionmaker
from apps.common.models.base_model import Base
from apps.common.models.users import User
from apps.common.models.products import Product
from apps.common.models.orders import Order
from sqlalchemy.orm import close_all_sessions
from config import create_app
from fastapi.testclient import TestClient
from sqlalchemy_utils import create_database, database_exists, drop_database

app = create_app()

login_data = {
    'username': 'admin@mail.com',
    'password': '12345'
}


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.print_test_info()
        cls.setup_database(cls.load_sample_data())
        cls.client = TestClient(app)
        cls.login()

    @classmethod
    def tearDownClass(cls):
        cls.clean_database()
        # Drop database if exists
        if database_exists(cls.engine.url):
            drop_database(cls.engine.url)

    @classmethod
    def setup_database(cls, data: dict):

        users = [User(**user) for user in data['users']]
        products = [Product(**product) for product in data['products']]

        cls.engine = create_test_engine()
        cls.Session = sessionmaker(cls.engine)

        # Create database
        if not database_exists(cls.engine.url):
            create_database(cls.engine.url)

        # Clean all tables on database (based on Base model)
        cls.clean_database()

        # Create all tables (based on Base model)
        Base.metadata.create_all(cls.engine)

        with cls.Session() as session:
            # Add data from input
            session.add_all(users)
            session.add_all(products)
            session.commit()

    @classmethod
    def login(cls):
        response = cls.client.post(
            'login',
            data=login_data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        cls.token = response.json()['access_token']

    @staticmethod
    def load_sample_data() -> list:
        with open(
            join(
                dirname(__file__),
                'input',
                'data.json'
            )
        ) as f:
            data = f.read()

        return json.loads(data)

    @classmethod
    def clean_database(cls):
        close_all_sessions()
        Base.metadata.drop_all(cls.engine)

    @classmethod
    def print_test_info(cls):
        print('----------------------------------------------------------------------')
        print(cls.test_name)
        print('----------------------------------------------------------------------')
