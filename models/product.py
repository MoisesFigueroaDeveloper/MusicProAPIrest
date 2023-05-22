from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[str] 
    name: str
    description: str
    category: str
    price: int
    stock: int
    
class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class Order(BaseModel):
    customer_id: str
    items: list[OrderItem]
    total_amount: float

class PaymentSession(BaseModel):
    order_id: str
    session_id: str