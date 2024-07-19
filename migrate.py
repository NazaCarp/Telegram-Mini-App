from db import Base, engine
from models import Counter

Base.metadata.create_all(bind=engine)