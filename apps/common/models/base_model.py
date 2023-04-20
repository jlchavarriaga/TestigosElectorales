from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime
from importlib import import_module
from os import listdir
from os.path import isdir, dirname, join


class Base(DeclarativeBase):
    """
    Declarative base class for sqlalchemy models
    """

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)


for file in listdir(dirname(__file__)):
    if not isdir(join(dirname(__file__), file)) and 'base' not in file:
        module = import_module('apps.common.models.%s' %
                               file.replace('.py', ''))
