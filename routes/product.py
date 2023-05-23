from fastapi import APIRouter, Response, status, HTTPException
from config.db import conn
from schemas.product import productEntity, productsEntity
from schemas.order import OrderItem, Order
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from schemas.product import Product

product = APIRouter()


# Encontrar todos los productos
@product.get('/products', response_model=list[Product], tags=["Products"])
def find_all_product():
    return productsEntity(conn.local.product.find())

# Encontrar productos por ID
@product.get('/products/{id}', response_model=list[Product], tags=["Products"])
def find_product(id: str):
    product = conn.local.product.find_one({"_id": ObjectId(id)})
    if product:
        return productEntity(product)
    else:
        return {"message": "Product not found"}

# Almacenar o crear nuevo producto
@product.post('/products', response_model=list[Product], tags=["Products"])
def create_product(product: Product):
    new_product = dict(product)
    del new_product["id"]

    inserted_id = conn.local.product.insert_one(new_product).inserted_id
    inserted_product = conn.local.product.find_one({"_id": inserted_id})
    return productEntity(product)

# Eliminar producto
@product.delete('/products/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
def delete_product(id: str):
    productEntity(conn.local.product.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

# Actualizar producto
@product.put('/products/{id}', response_model=list[Product], tags=["Products"])
def update_product(id: str, product: Product):
    conn.local.product.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(product)})
    return productEntity(conn.local.product.find_one({"_id": ObjectId(id)}))

