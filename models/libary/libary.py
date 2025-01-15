from database import Base
from sqlalchemy import Column, Integer

class Libary(Base):
    __tablename__ = "libary"
    book_id = Column(Integer, nullable=False)
    count_book = Column(Integer, nullable=False)
    author_id = Column(Integer, nullable=False)