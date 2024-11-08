from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class UserProfile(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str



class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None