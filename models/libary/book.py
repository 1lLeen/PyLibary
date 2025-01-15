from datetime import datetime
from database import Base
from sqlalchemy import Column, String, Integer, DateTime

class Book:
    id:Column(Integer, primary_key=True, nullable=False,index=True)
    book_name:Column(String)
    description:Column(String)
    date_public:Column(DateTime)
    genre_id:Column(Integer)