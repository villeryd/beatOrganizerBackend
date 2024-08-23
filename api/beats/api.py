from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from libraries.beats import (Beat, BeatUpdates)


app = APIRouter(
    prefix="/beats",
    tags=["beats"],
)


@app.get
@app.get('/')
async def root():
    return {"message": 'hello world'}


@app.get("/get-beat/{beat_Id}")
def get_beat(beat_Id: int):
    return beats[beat_Id]


@app.post("/create-beat")
async def create_beat(beat_object: Beat, response_model=Beat):
    return beat_object
