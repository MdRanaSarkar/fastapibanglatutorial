from database import sessionLocal
from fastapi import FastAPI
from sqlalchemy.orm import Session

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.get("/")
async def read_root():
    return {"msg": "Hello World"}