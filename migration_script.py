from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Counter, Referral
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Eliminar las tablas existentes
Base.metadata.drop_all(bind=engine)

# Crear las tablas nuevamente
Base.metadata.create_all(bind=engine)

# Agregar un registro inicial
db = SessionLocal()
counter = Counter(user_id=1, score=0, secondarycount=0, tap=1)
db.add(counter)
db.commit()

referral = Referral(user_id=1, from_user='', referralscount=0, referrals='')
db.add(referral)
db.commit()

db.close()