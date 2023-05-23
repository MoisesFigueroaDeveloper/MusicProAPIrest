from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    description: str
    category: str
    price: int
    stock: int

def productEntity(item) -> dict:
    return {
        "id" : str(item["_id"]),
        "name" : item["name"],
        "description" : item["description"],
        "category" : item["category"],
        "price" : item["price"],
        "stock" : item["stock"],
    }
    
def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]

