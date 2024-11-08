from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"msg": "Hlw World",}


@app.get("/books")
async def bookname():
    return {"Books": "Easily CSE Learn",}


    @app.get("/items/{item_name}")
    async def item_name(item_name: str):
        return {"item-name": item_name}