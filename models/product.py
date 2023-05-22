from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[str] 
    sku: int
    name: str
    description: str
    category: str
    price: int
    stock: int
    
class OrderItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    products: list[OrderItem]
    buyOrder: int
    sessionId: int
    total_amount: float