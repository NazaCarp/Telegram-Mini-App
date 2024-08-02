from db import Base, engine
from models import Base, Counter, Referral

Base.metadata.create_all(bind=engine)