from fastapi import FastAPI

app = FastAPI()


@app.get("/book/{book_id}")
async def read_book(book_id : int):
    return {
            "BookID" : book_id,
            "Title":  " The great Gatsby",
            "Author": "F. Scott Fitzgerald",

        }