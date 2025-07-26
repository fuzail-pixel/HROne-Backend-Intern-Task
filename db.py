import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = "hrone_task_db"

client = None
db = None

async def connect_db():
    global client, db
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
        db = client[DB_NAME]
        print("Connected to MongoDB")
    except Exception as e:
        print(f" MongoDB connection error: {e}")

async def close_db():
    global client
    if client:
        client.close()
        print(" Disconnected from MongoDB")

def get_db():
    return db
