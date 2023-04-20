from apps.common.models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Department(Base):

    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'))
    cities = relationship("City", back_populates='Department', cascade="all, delete")
