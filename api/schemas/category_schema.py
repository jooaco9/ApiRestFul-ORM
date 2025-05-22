from sqlmodel import SQLModel, Field

# Schema para las categorias
class Category(SQLModel):
    name: str = Field("Nombre de la categoria")