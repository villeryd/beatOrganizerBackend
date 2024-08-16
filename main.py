from fastapi import FastAPI
import datetime

app = FastAPI()

beats = {
    1: {
        "title": "fire",
        "date": datetime.datetime.now().isoformat(),
        "tags": {"trap", "fast", "drill"},
        "genre": 'Hip-Hop',
        "artwork": "",
        "mp3": {}
    }
}


@app.get('/')
async def root():
    return {"message": 'hello world'}


@app.get("/get-beat/{beat_Id}")
def get_beat(beat_Id: int):
    return beats[beat_Id]
