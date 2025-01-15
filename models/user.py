from sqlalchemy import Column, String, Integer
from database import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username:Column(String)
    password:Column(String)
    is_admin:Column(Integer)

    