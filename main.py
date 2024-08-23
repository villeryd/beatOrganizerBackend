
from fastapi import FastAPI
import datetime


import api.beats.api as beats

app = FastAPI(
    title="beats API"
)

app.include_router(beats.app)
