from database import Base
from sqlalchemy import Column, Integer

class Libary:
    book_id:Column(Integer, nullable=False)
    count_book:Column(Integer, nullable=False)
    author_id:Column(Integer, nullable=False)