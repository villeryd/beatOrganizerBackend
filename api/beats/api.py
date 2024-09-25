from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from libraries.beats import (BeatBase)
from db.models.beats import (Beat)
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
    prefix="/beats",
    tags=["beats"],
)

db_dependency = Annotated[Session, Depends(get_db)]


@app.post('/beats/')
async def create_beat(beat: BeatBase, db: db_dependency):
    db_beat = Beat(
        title=beat.title,
        genre=beat.genre,
        artwork=beat.artwork,
    )
    db.add(db_beat)
    db.commit()
    db.refresh(db_beat)
    return db_beat
