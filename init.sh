alembic upgrade head
paver apps.common.commands.tasks.admin.create_admin -u admin -p 12345 -e admin@mail.com
uvicorn config:create_app --factory --reload --port 8080 --host 0.0.0.0