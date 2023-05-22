from fastapi import FastAPI 
from routes.product import product
from docs import tags_metadata

app = FastAPI(
    title= "Music Pro",
    description= "Es una simple API rest con una integracion de webpay",
    version= "0.0.1",
    openapi_tags= tags_metadata
)

app.include_router(product)
