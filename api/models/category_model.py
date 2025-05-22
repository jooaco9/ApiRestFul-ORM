from sqlmodel import SQLModel, Field

# Moedelo Category
class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: int = Field(primary_key=True, description="Id de la categoria")
    name: str = Field(description="Nombre de la categoria")