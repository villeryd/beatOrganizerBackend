from fastapi import FastAPI
import datetime
from schemas import Beat

app = FastAPI()

beats = []


@app.get('/')
async def root():
    return {"message": 'hello world'}


@app.get("/get-beat/{beat_Id}")
def get_beat(beat_Id: int):
    return beats[beat_Id]


@app.post("/create-beat")
async def create_beat(beat_object: Beat):
    beats.append(beat_object)
    return beats
