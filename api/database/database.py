from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Creacion del Enginte contra la DB
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost/masterpodcast'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Genero la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia
def get_db():
    # Creamos la session
    db = SessionLocal()
    try:
        # Devolvemos la sesion
        yield db
    finally:
        # Cerrar sesion al finalizar el proceso
        db.close()