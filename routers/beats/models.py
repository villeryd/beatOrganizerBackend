from fastapi import FastAPI
from fastapi import APIRouter
import datetime
from pydantic import BaseModel, HttpUrl
from uuid import uuid4

router = APIRouter()


class Beat(BaseModel):
    title: str
    date: datetime.datetime | None = datetime.datetime.now().isoformat()
    tags: list[str] = []
    genre: str
    artwork: HttpUrl | None = None


class BeatUpdates(Beat):
    id: int
    likes: int
