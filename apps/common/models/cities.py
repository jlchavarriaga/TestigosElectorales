from apps.common.models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    department_id = Column(Integer, ForeignKey('department.id'))
    localities = relationship(
        "Locality", back_populates='City', cascade="all, delete")
    name = Column(String(255), nullable=False)
