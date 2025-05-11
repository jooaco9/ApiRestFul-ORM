from sqlalchemy.exc import SQLAlchemyError
import pytest
from api import engine
from sqlalchemy import text

# Comprobacion del a conexino contra la DB
def test_connection_db_ok():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("select name from categories"))
            rows = result.all()
            assert len(rows) > 0
    except SQLAlchemyError as excinfo:
        pytest.fail(f"Se ha producido un error en la conexion o en la consulta: {excinfo}")