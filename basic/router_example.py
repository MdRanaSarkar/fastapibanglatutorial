from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"msg": "Welcome to our Websites!"}
    

@app.get("/item/{item_id}")
async def read_item(item_id : int):
    return {"Item ID": item_id}