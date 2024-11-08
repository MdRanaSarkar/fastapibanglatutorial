from pydantic import BaseModel,Field

# class Book(BaseModel):
#     title:str
#     author:str
#     year:int


# modification of the book model's fields
class Book(BaseModel):
    title:str=Field(..., min_length=1, max_length=100)
    author:str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., gt=2000, lt=2100)