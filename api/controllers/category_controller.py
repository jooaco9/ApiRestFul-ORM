from sqlalchemy import select
from api import CategoryModel

def get_categories(db):
    # Crear la consulta
    stmt = select(CategoryModel)

    # Lista de categorias
    result = db.scalars(stmt)
    categories = result.all()

    return categories