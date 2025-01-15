from sqlalchemy import Column, Integer, DateTime
from database import Base
class Control(Base):
    __tablename__ = 'control'
    user_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=False)
    issued = Column(DateTime, nullable=False)
    until = Column(DateTime, nullable=False)
    left_days = Column(DateTime, nullable=False)