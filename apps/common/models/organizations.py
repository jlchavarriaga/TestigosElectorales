from apps.common.models.base_model import Base
from sqlalchemy import Column, Integer, String


class Organization(Base):

    __tablename__ = 'political_organizations'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)

    # TODO 1: Search for uploading images of parties in this table
