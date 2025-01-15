from database import Base
from sqlalchemy import Column, String

class Genre:
    name:Column(String)