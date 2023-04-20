from apps.common.models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Locality(Base):

    __tablename__ = 'localities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    city_id = Column(Integer, ForeignKey('city.id'))
    name = Column(String(255), nullable=False)

# TODO 2: Update draw diagrams with locality model