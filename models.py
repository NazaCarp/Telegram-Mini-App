from sqlalchemy import Column, BigInteger, Integer, Float, DateTime, String, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Counter(Base):
    __tablename__ = "counters"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, unique=True, index=True)
    name = Column(String)
    username = Column(String)
    score = Column(Float)
    secondarycount = Column(Integer)
    timestamp = Column(DateTime)
    tap = Column(Integer)
    energy_limit = Column(Integer)
    recharge_speed = Column(Integer)
    profit_per_hour = Column(Float)
    daily_reward_streak = Column(Integer)
    last_daily_reward_claimed = Column(DateTime)
    completed_tasks = Column(JSON, default={})  # Nuevo campo para almacenar tareas completadas


class Referral(Base):
    __tablename__ = 'referrals'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    name = Column(String, default='')
    from_user = Column(String, default='')
    referrals_count = Column(Integer, default=0)
    referrals_name = Column(String, default='')
    referrals_id = Column(String, default=None)


class MineLevels(Base):
    __tablename__ = 'mine_levels'
    user_id = Column(BigInteger, primary_key=True, index=True)
    clubs = Column(JSONB, default={})