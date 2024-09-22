
from fastapi import FastAPI, HTTPException, Depends
import datetime


import api.beats.api as beatsAPI
from db.database import engine
from db.models import users, beats

# users.Base.metadata.create_all(bind=engine)
beats.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="beats API"
)

app.include_router(beatsAPI.app)
