from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from libraries.beats import (Beat, BeatBase)
from database import engine, SessionLocal


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


@app.post('/beats/')
async def create_beat(Beat: BeatBase):
