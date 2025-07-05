from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage for items
items = []

# Pydantic model for an item
class Item(BaseModel):
    name: str
    description: str
    price: float

@app.get("/test")
def read_test():
    return {"message": "This is a test API"}

@app.get("/osfp")
def read_test():
    return {"message": "Welcome to OSFP Bootcamp 2025"}


@app.get("/")
def read_root():
    return {"message": "https://www.youtube.com/babarzahoor <br> <br> https://github.com/DevOps-With-Babar-Zahoor/RamadanBootCamp2025"}
    # return {"message": "Welcome to the FastAPI application!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if 0 <= item_id < len(items):
        return items[item_id]
    return {"error": "Item not found"}

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item added successfully", "item": item}
