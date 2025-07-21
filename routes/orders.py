from fastapi import APIRouter, HTTPException, Path, Query
import db  
from schemas.order import OrderCreate, OrderResponse
from typing import List
from datetime import datetime
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=OrderResponse, status_code=201)
async def create_order(order: OrderCreate):
    total_price = 0.0
    for pid in order.products:
        product = await db.db["products"].find_one({"_id": ObjectId(pid)})
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with ID {pid} not found")
        total_price += product["price"]

    order_doc = {
        "user_id": order.user_id,
        "products": order.products,
        "total_price": total_price,
        "created_at": datetime.utcnow()
    }

    result = await db.db["orders"].insert_one(order_doc)
    order_doc["_id"] = str(result.inserted_id)
    return order_doc


@router.get("/{user_id}", response_model=List[OrderResponse])
async def get_orders(
    user_id: str = Path(...),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)
):
    cursor = db.db["orders"].find({"user_id": user_id}).skip(offset).limit(limit)
    results = []
    async for order in cursor:
        order["_id"] = str(order["_id"])
        results.append(order)
    return results
