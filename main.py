from fastapi import FastAPI
from routes.products import router as product_router
from routes.orders import router as order_router
from db import connect_db, close_db  

app = FastAPI()

# Register routers
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(order_router, prefix="/orders", tags=["Orders"])

# MongoDB connection lifecycle
@app.on_event("startup")
async def startup_event():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db()
