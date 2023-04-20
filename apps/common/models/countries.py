from apps.common.models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Country(Base):

    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    departments = relationship("Department", back_populates='Country', cascade="all, delete")

    # TODO 3: Update diagrams with country model