from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    
    return {"msg": "Hi Welcome to my Easily CSE learning channel"}