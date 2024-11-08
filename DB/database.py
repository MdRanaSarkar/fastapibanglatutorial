from fastapi import Depends, FastAPI , HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated

    
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(connect_args=connect_args, url=sqlite_url)


def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    

sessionDep = Annotated[Session, Depends(get_session)]


app = FastAPI()


@app.on_event("startup")
def on_startapp():
    create_db_and_tables()


class PersonInfo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str
    