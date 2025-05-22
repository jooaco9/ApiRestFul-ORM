from fastapi import APIRouter, status, HTTPException, Depends, Path
from typing_extensions import Annotated
from sqlmodel import Session
from api import category_controller, get_db
from api import CategoryModel, CategorySchema

# Enrutador para difinir los endpoints
router = APIRouter()

# Endopoint para devolver todas las categorias
@router.get("", response_model=list[CategoryModel], status_code=status.HTTP_200_OK,
            summary="Obtiene todas las categorias"
            )
async def get_categories(db: Session = Depends(get_db)):
    return await category_controller.get_categories(db)

# Endopoint para devolver una categoria sola
@router.get("/{category_id}", response_model=CategoryModel, status_code=status.HTTP_200_OK,
            summary="Obtiene una categoria por el id"
            )
async def get_category(category_id: Annotated[int, Path(
                                    description="Id de la categoria que se va a actualizar",
                                    gt=0
                                    )],
                        db: Session = Depends(get_db)):
    category = await category_controller.get_category(category_id, db)

    # Si no esta la categoria, devovles una excepcion 404
    if not category:
        raise HTTPException(status_code=404, detail=f"No hay una categoria con el id {category_id}")

    return category

# Endopoint para agregar una categoria
@router.post("", response_model=CategoryModel, status_code=status.HTTP_200_OK,
             summary="Agrega una categoria"
             )
async def write_categories(categorie: CategorySchema, db: Session = Depends(get_db)):
    return await category_controller.write_category(categorie, db)

# Endopoint para actualizar una categoria
@router.put("/{category_id}", response_model=CategoryModel, status_code=status.HTTP_200_OK)
async def update_categories(category_id: Annotated[int, Path(
                                        description="Id de la categoria que se va a actualizar",
                                        gt=0
                                        )],
                            category: CategorySchema, db: Session = Depends(get_db)):
    update_category = await category_controller.update_category(category_id, category, db)

    # Si no esta la categoria, devovles una excepcion 404
    if not update_category:
        raise HTTPException(status_code=404, detail=f"No hay una categoria con el id {category_id}")

    return update_category

# Endopint para borrar una categoria
@router.delete("/{category_id}", response_model=CategoryModel, status_code=status.HTTP_200_OK,
            summary="Se borra categoria por id")
async def delete_categories(category_id: Annotated[int, Path(
                                    description="Id de la categoria que se va a actualizar",
                                    gt=0
                                    )],
                        db: Session = Depends(get_db)):
    category = await category_controller.delete_category(category_id, db)

    if not category:
        raise HTTPException(status_code=404, detail=f"No hay una categoria con el id {category_id}")

    return category