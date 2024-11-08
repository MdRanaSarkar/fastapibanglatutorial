from fastapi import FastAPI
from models import Book 

app = FastAPI()



@app.get("/")
async def home(book:Book):
    return {"msg": "welcome to our app "}
    
@app.post("/book")
async def create_book(book:Book):
    return book




    
@app.get("/all_books", response_model=list[Book])
async def all_books()->any:
    return [{
        "title": "string",
    "author": "string",
        "year": int
        }]