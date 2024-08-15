from sqlalchemy import Column, BigInteger, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Counter(Base):
    __tablename__ = "counters"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, unique=True, index=True)
    name = Column(String)
    username = Column(String)
    score = Column(Integer, default=0)
    secondarycount = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)
    tap = Column(Integer, default=1)
    energy_limit = Column(Integer, default=1000)
    recharge_speed = Column(Integer, default=1)


class Referral(Base):
    __tablename__ = 'referrals'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(String, nullable=False)
    name = Column(String, default='')
    from_user = Column(String, default='')
    referrals_count = Column(Integer, default=0)
    referrals_name = Column(String, default='')
    referrals_id = Column(String, default=None)


class MineLevels(Base):
    __tablename__ = 'mine_levels'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey('counters.user_id'), index=True)
    club_id = Column(String, index=True)  # Identificador único del rectángulo
    level = Column(Integer, default=1)

    user = relationship('Counter', backref='mine_levels')