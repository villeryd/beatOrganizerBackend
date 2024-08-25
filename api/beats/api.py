from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from libraries.beats import (Beat,)


app = APIRouter(
    prefix="/beats",
    tags=["beats"],
)
