from db import Base, engine
from models import Base, Counters, Referral

Base.metadata.create_all(bind=engine)