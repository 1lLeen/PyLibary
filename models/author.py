from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Author(Base):
    id:Column(Integer,primary_key=true,nullable=false,index=true)
    full_name:Column(String)
    biography:Column(String)
    date_of_birth:Column(DateTime)
