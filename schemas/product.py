from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    size: Optional[str] = None

class ProductResponse(ProductCreate):
    id: str = Field(..., alias="_id")
