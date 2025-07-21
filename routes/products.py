from fastapi import APIRouter, HTTPException, Query
import db  
from schemas.product import ProductCreate, ProductResponse
from typing import List, Optional
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=ProductResponse, status_code=201)
async def create_product(product: ProductCreate):
    product_dict = product.dict()
    result = await db.db["products"].insert_one(product_dict) 
    product_dict["_id"] = str(result.inserted_id)
    return product_dict
