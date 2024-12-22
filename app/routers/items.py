from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Item

router = APIRouter(prefix="/items", tags=["items"])

# Dummy database
items_db = []

@router.get("/", response_model=List[Item])
async def get_items():
    return items_db

@router.post("/", response_model=Item, status_code=201)
async def create_item(item: Item):
    # Simple ID generation
    item.id = len(items_db) + 1
    items_db.append(item)
    return item

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found") 