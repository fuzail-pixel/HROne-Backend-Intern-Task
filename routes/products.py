from fastapi import APIRouter, HTTPException, Query
from db import get_db
from schemas.product import ProductCreate, ProductResponse
from typing import List, Optional
from bson import ObjectId
import re

router = APIRouter()

@router.post("/", response_model=ProductResponse, status_code=201)
async def create_product(product: ProductCreate):
    db_instance = get_db()
    product_dict = product.dict()

    result = await db_instance["products"].insert_one(product_dict)
    product_dict["_id"] = str(result.inserted_id)  # ✅ Fix: convert ObjectId to string

    return ProductResponse(**product_dict)

@router.get("/", response_model=List[ProductResponse], status_code=200)
async def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = Query(default=10, ge=1),
    offset: int = Query(default=0, ge=0)
):
    db_instance = get_db()
    query = {}

    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}
    if size:
        query["size"] = size

    cursor = db_instance["products"].find(query).skip(offset).limit(limit)
    products = []
    async for product in cursor:
        product["_id"] = str(product["_id"])  # ✅ Ensure string ID for response model
        products.append(ProductResponse(**product))

    return products
