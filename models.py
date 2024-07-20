from sqlalchemy import Column, BigInteger, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Counter(Base):
    __tablename__ = 'counters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, unique=True)
    value = Column(Integer, default=0)