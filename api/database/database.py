from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.exc import SQLAlchemyError

# Creacion del Enginte contra la DB
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root@localhost/masterpodcast'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Dependencia
def get_db():
    # Creamos la session
    try:
        with Session(engine) as session:
            yield session
    except SQLAlchemyError as e:
        # Manejo de errores de SQLAlchemy
        print(f"Error al conectar con la base de datos: {e}")
        raise
