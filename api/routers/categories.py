from fastapi import APIRouter, status, HTTPException, Depends, Path
from typing_extensions import Annotated
from sqlmodel import Session
from api import category_controller, get_db
from api import CategoryModel, CategorySchema

# Enrutador para difinir los endpoints
router = APIRouter()

@router.get("", response_model=list[CategoryModel], status_code=status.HTTP_200_OK)
async def get_categories(db: Session = Depends(get_db)):
    return await category_controller.get_categories(db)

@router.post("", response_model=CategoryModel, status_code=status.HTTP_200_OK)
async def write_categories(categorie: CategorySchema, db: Session = Depends(get_db)):
    return await category_controller.write_category(categorie, db)

@router.put("/{category_id}", response_model=CategoryModel, status_code=status.HTTP_200_OK)
async def update_categories(category_id: Annotated[int, Path(
                                description="Id de la categoria que se va a actualizar",
                                gt=0
                            )], category: CategorySchema, db: Session = Depends(get_db)):
    update_category = await category_controller.update_category(category_id, category, db)

    # Verficiar que devuelva una categoria
    if not update_category:
        raise HTTPException(status_code=404, detail=f"No hay una categoria con el id {category_id}")

    return update_category

@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_categories():
    pass