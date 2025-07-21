# HROne Backend Internship Task - Ecommerce API

## Overview
This is a FastAPI-based ecommerce backend application built for the HROne internship task. The application provides REST APIs for managing products and orders, similar to platforms like Flipkart/Amazon.

## Features
- ✅ Create and list products with filtering capabilities
- ✅ Create orders and retrieve user order history
- ✅ MongoDB integration for data persistence
- ✅ Query parameters for filtering and pagination
- ✅ RESTful API design following the specified requirements

## Tech Stack
- **Framework**: FastAPI (Python 3.10+)
- **Database**: MongoDB with PyMongo/Motor
- **Deployment**: Render/Railway (Free Plan)
- **Database Hosting**: MongoDB Atlas M0 (Free Tier)

## API Endpoints

### Products

#### Create Product
- **Endpoint**: `POST /products`
- **Request Body**:
```json
{
    "name": "Product Name",
    "price": 299.99,
    "quantity": 100,
    "size": "large",
    "description": "Product description"
}
```
- **Response**: `201 CREATED`

#### List Products
- **Endpoint**: `GET /products`
- **Query Parameters** (optional):
  - `name`: Filter by product name (supports partial/regex search)
  - `size`: Filter by product size (e.g., `size=large`)
  - `limit`: Number of documents to return
  - `offset`: Number of documents to skip for pagination
- **Response**: `200 OK`

### Orders

#### Create Order
- **Endpoint**: `POST /orders`
- **Request Body**:
```json
{
    "user_id": "user123",
    "items": [
        {
            "product_id": "product_id_here",
            "bought_quantity": 2
        }
    ],
    "user_address": {
        "city": "Delhi",
        "country": "India",
        "zip_code": "110001"
    }
}
```
- **Response**: `201 CREATED`

#### Get User Orders
- **Endpoint**: `GET /orders/{user_id}`
- **Query Parameters** (optional):
  - `limit`: Number of documents to return
  - `offset`: Number of documents to skip for pagination
- **Response**: `200 OK`

## Project Structure
```
├── main.py                 # FastAPI application entry point
├── db.py                   # MongoDB database connection
├── routes/
│   ├── orders.py          # Order API endpoints
│   └── products.py        # Product API endpoints
├── schemas/
│   ├── order.py           # Order Pydantic models
│   └── product.py         # Product Pydantic models
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Database Schema

### Products Collection
```json
{
    "_id": "ObjectId",
    "name": "string",
    "price": "number",
    "quantity": "number",
    "size": "string",
    "description": "string",
    "created_at": "datetime"
}
```

### Orders Collection
```json
{
    "_id": "ObjectId",
    "user_id": "string",
    "items": [
        {
            "product_id": "ObjectId",
            "bought_quantity": "number"
        }
    ],
    "user_address": {
        "city": "string",
        "country": "string",
        "zip_code": "string"
    },
    "total_amount": "number",
    "created_at": "datetime"
}
```

## Prerequisites
- Python 3.10 or higher
- MongoDB Atlas account (free tier)
- Git

## Deployment

### MongoDB Atlas Setup
1. Create a free MongoDB Atlas account
2. Create a new M0 (free) cluster
3. Create a database user and get the connection string
4. Whitelist your IP address (or use 0.0.0.0/0 for development)

### Render Deployment
1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add environment variables in Render dashboard

## Key Implementation Features

### Filtering & Search
- **Product name search**: Implements regex-based partial matching
- **Size filtering**: Exact match filtering for product sizes
- **Pagination**: Offset-based pagination sorted by `_id`

### Data Validation
- Pydantic models for request/response validation
- Proper error handling and HTTP status codes
- Input sanitization for MongoDB queries

### Database Optimization
- Efficient MongoDB queries with proper indexing
- Optimized aggregation pipelines for order retrieval
- Connection pooling for better performance

## Testing
The application is designed to be tested by automated scripts that will:
1. Test all API endpoints with specified request/response formats
2. Verify HTTP status codes
3. Validate data structure and MongoDB operations

## Error Handling
- Comprehensive error responses with appropriate HTTP status codes
- Validation errors for malformed requests
- Database connection error handling
- Resource not found handling

## Performance Considerations
- Database queries are optimized for the expected load
- Proper indexing on frequently queried fields
- Connection pooling for database operations
- Efficient pagination implementation

## Contact
For any questions regarding this implementation, please contact:
- **Developer**: Fuzail Rehman
- **Email**: fuzailcl@gmail.com