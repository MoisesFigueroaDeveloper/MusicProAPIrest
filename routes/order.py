from fastapi import APIRouter
from config.db import conn
from schemas.product import productEntity
from schemas.order import OrderItem, Order
from bson import ObjectId

order = APIRouter()

# Se crea la orden con el producto 
@order.post('/orders', response_model=Order, tags=["Orders"])
def create_order(order_item: OrderItem):
    product_id = order_item.product_id
    quantity = order_item.quantity

    product = conn.local.product.find_one({"_id": ObjectId(product_id)})
    if not product:
        return {"message": "Product not found"}

    order = Order(
        id="123",  # Genera un ID único para el pedido
        customer_id="456",  # ID del cliente asociado al pedido
        items=[OrderItem(product_id=product_id, quantity=quantity, price=product["price"])],
        total_amount=product["price"] * quantity
    )

    # Aquí puedes realizar acciones adicionales, como almacenar el pedido en la base de datos

    return order