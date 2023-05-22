from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[str] 
    name: str
    description: str
    category: str
    price: int
    stock: int
    
