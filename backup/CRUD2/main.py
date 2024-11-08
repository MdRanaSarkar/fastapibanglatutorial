from database import SessionLocal
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return {"users": "rana"}