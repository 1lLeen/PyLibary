from database import Base
from sqlalchemy import Column, String, Integer

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)