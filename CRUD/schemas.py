from pydantic import BaseModel

class UserProfileBase(BaseModel):
    id: int | None
    name: str | None
    age : int | None
    secret_name: str 