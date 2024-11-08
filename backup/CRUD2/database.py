from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine   

class Base(DeclarativeBase): 
    pass

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)