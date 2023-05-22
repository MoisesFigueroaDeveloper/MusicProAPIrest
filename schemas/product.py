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