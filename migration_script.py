from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Counter
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Eliminar las tablas existentes
#Base.metadata.drop_all(bind=engine, tables=[Counter.__table__])
Base.metadata.drop_all(bind=engine)

# Crear las tablas nuevamente
Base.metadata.create_all(bind=engine)