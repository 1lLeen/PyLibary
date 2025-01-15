from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    full_name = Column(String)
    biography = Column(String)
    date_of_birth = Column(DateTime)
