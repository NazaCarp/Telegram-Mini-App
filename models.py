from sqlalchemy import Column, BigInteger, Integer, DateTime, String
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Counter(Base):
    __tablename__ = 'counters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, unique=True)
    name = Column(String, default='')
    score = Column(Integer, default=0)
    secondarycount = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)
    tap = Column(Integer, default=1)

class Referral(Base):
    __tablename__ = 'referrals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    name = Column(String, default='')
    from_user = Column(String, default='')
    referrals_count = Column(Integer, default=0)
    referrals_name = Column(String, default='')
    referrals_id = Column(BigInteger, default=None)