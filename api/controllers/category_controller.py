from sqlmodel import select
from api import CategoryModel, CategorySchema

async def get_categories(db):
    # Crear la consulta
    stmt = select(CategoryModel)

    # Lista de categorias
    result = db.exec(stmt)
    categories = result.all()

    return categories

async def write_category(category: CategorySchema, db):
    # Creo el modelo ORM a partir del schema
    category_model = CategoryModel(name=category.name)
    print(category_model)

    # Agregamos la categoria a la sesion
    db.add(category_model)

    # Confirmo el cambio
    db.commit()

    # Se refresca para obtener el id generado
    db.refresh(category_model)

    return category_model

async def update_category(category_id, category: CategorySchema, db):
    # Verificar que haya categoria con el id de category
    existing_category = db.get(CategoryModel, category_id)
    if not existing_category:
        return None

    # Actualizar la category
    existing_category.name = category.name

    # Confirmo los cambios
    db.commit()

    # Refrescar para obtener los datos actualizados
    db.refresh(existing_category)

    return existing_category
