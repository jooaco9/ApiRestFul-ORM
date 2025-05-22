from fastapi import APIRouter, status, HTTPException, Depends
from sqlmodel import Session
from api import category_controller, get_db
from api import CategoryModel

# Enrutador para difinir los endpoints
router = APIRouter()

@router.get("", response_model=list[CategoryModel], status_code=status.HTTP_200_OK)
async def get_categories(db: Session = Depends(get_db)):
    return category_controller.get_categories(db)

@router.post("/", status_code=status.HTTP_200_OK)
async def write_categories(categorie: str):
    pass

@router.put("/", status_code=status.HTTP_200_OK)
async def update_categories():
    pass

@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_categories():
    pass