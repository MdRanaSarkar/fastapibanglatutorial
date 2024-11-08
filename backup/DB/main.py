from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_item, get_items, create_item
from schemas import Item
from models import ItemCreate
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/items/", response_model= Item)
def new_create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

@app.get("/items/{item_id}", response_model= Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items