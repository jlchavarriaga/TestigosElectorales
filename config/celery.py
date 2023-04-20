from celery import Celery
from celery.schedules import crontab
from os import environ
from apps.mailer.tasks import send_orders_report, send_email
import config.environment as env
import time

redis_uri = f"redis://{env.REDIS}"


celery_app = Celery(
    'config',
    broker=f"{redis_uri}/0",
    backend=f"{redis_uri}/1",
    include=[]
)

environ['TZ'] = env.ENVIRONMENT['TIMEZONE']
time.tzset()

celery_app.conf.timezone = environ.get('TIMEZONE')
celery_app.conf.enable_utc = True


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='*/15'),
        orders_report.s(),
    )


@celery_app.task
def validation_email(*args, **kwargs):
    send_email(*args, **kwargs)


@celery_app.task
def orders_report():
    send_orders_report()
