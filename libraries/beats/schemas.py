from fastapi import FastAPI
from fastapi import APIRouter
import datetime
from pydantic import BaseModel, HttpUrl
from uuid import uuid4

router = APIRouter()


class BeatBase(BaseModel):
    title: str
    genre: str
    artwork: HttpUrl | None = None


class BeatCreate(BeatBase):
    pass


class Beat(BeatBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    beats: list[Beat] = []

    class Config:
        orm_mode = True
