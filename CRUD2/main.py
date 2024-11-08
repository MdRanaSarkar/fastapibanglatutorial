from database import  get_db
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Item


app = FastAPI()


@app.get("/")
async def read_root():
    return {"msg": "Hello World"}

@app.post("/create_item")
async def create_item(item:Item, db: Session = Depends(get_db)):
    new_item = Item( name=item.name, description=item.description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
    