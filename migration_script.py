from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Counter
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Eliminar la tabla existente
Base.metadata.drop_all(bind=engine, tables=[Counter.__table__])

# Crear la tabla nuevamente
Base.metadata.create_all(bind=engine)

# Agregar un registro inicial
db = SessionLocal()
counter = Counter(user_id="initial_user", value=0)
db.add(counter)
db.commit()
db.close()