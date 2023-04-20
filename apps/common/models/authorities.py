from apps.common.models.base_model import Base
from sqlalchemy import Column, Integer, String


class Authority(Base):

    __tablename__ = 'authorities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)

