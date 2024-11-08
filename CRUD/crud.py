from fastapi import Depends, FastAPI, HTTPException, Query
from models import UserProfile, Item
from database import create_db_and_tables, get_session
from typing import Annotated
from sqlmodel import Session, create_engine, select
from schemas import UserProfileBase


SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/create_new_user")
def create_userprofile(userprofile: UserProfile, session: SessionDep)-> UserProfile:
    session.add(userprofile)
    session.commit()
    session.refresh(userprofile)
    return userprofile


@app.get("/show_all_profiles")
def show_all_profile(session: SessionDep,
                      offset: int = 0,
                        limit: Annotated[int, Query(le=100)] = 100,
                        ) -> list[UserProfile]:
    user_profiles = session.exec(select(UserProfile).offset(offset).limit(limit)).all()
    return user_profiles


@app.get('/userprofile/{user_id}')
def show_user_profile(user_id: int, session: SessionDep)-> UserProfile:
    user_profile = session.get(UserProfile, user_id)
    if user_profile is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_profile



@app.put('/userprofile/{user_id}')
def userprofile_update(user_id:int, user_update:UserProfileBase, session: SessionDep)-> UserProfile:
    user_profile = session.get(UserProfile, user_id)
    if user_profile is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user_profile, key, value)
    session.commit()
    session.refresh(user_profile)
    return user_profile


# Delete user profile


@app.delete("/userprofile/{s}")
def delete_profile(user_id: int, session: SessionDep):
    user_profile = session.get(UserProfile, user_id)
    if user_profile is None:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user_profile)
    session.commit()
    return {"Ok": True}




# check item model CRUD

@app.post("/create_items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}