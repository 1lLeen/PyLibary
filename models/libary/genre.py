from database import Base
from sqlalchemy import Column, String

class Genre(Base):
    __tablename__ = "genres"
    name = Column(String)