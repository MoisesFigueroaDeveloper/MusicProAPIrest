from pydantic import BaseModel
from typing import List
from .product import Product

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class Order(BaseModel):
    id: str
    customer_id: str
    items: List[OrderItem]
    total_amount: float
