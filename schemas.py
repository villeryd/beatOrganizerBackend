from fastapi import FastAPI
import datetime
from pydantic import BaseModel, HttpUrl
from uuid import uuid4


class Beat(BaseModel):
    title: str
    date: None = datetime.datetime.now().isoformat()
    tags: list[str] = []
    genre: str
    artwork: HttpUrl | None = None


class BeatUpdates(Beat):
    id: int
    likes: int
