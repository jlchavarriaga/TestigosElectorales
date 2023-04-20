from fastapi import FastAPI
from config.postgres import Postgres

Session = Postgres.create_session_factory()


def create_app():
    app = FastAPI()

    from apps.api.routers import main, users, products, auth, orders

    app.include_router(main.router)
    app.include_router(users.router)
    app.include_router(auth.router)
    app.include_router(products.router)
    app.include_router(orders.router)

    return app
