import os
from config.environment import ENVIRONMENT as env
from datetime import datetime
import pytz


def local_now():
    """datetime.datetime.now of local timezone

    Returns:
        datetime.datetime:
    """
    timezone = env['TIMEZONE'] or os.getenv(
        'TIMEZONE', 'America/Bogota')

    now = datetime.now(pytz.timezone(
        timezone
    ))
    return datetime(
        year=now.year,
        month=now.month,
        day=now.day,
        hour=now.hour,
        minute=now.minute,
        second=now.second,
        microsecond=now.microsecond
    )
