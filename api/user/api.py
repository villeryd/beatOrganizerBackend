from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from libraries.users import (User)
from db.models.users import (UserBase)
from db.database import engine, SessionLocal
from typing import List, Annotated
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = APIRouter(
    prefix="/user",
    tags=["user"],
)

db_dependency = Annotated[Session, Depends(get_db)]


@app.post('/create_new')
async def create_new_user(user: UserBase, db: db_dependency):
    db
    return
