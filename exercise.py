from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Storage
items = {}
item_id_counter = 1


class Item(BaseModel):
    name: str
    price: float
    quantity: int
    category: str