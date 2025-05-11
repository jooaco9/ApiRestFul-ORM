from typing import Union
from pydantic import BaseModel

# Schemas de categoria
class CategoryBase(BaseModel):
    name:str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes  = True