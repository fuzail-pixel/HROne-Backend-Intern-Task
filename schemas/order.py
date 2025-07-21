from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: str
    products: List[str]

class OrderResponse(BaseModel):
    order_id: str = Field(..., alias="_id")
    user_id: str
    products: List[str]
    total_price: float
    created_at: datetime
