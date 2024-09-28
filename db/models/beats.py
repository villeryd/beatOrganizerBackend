from fastapi import APIRouter, Depends, HTTPException
from libraries.beats.schemas import Beat

from sqlalchemy import Boolean, Column, String, ForeignKey, Integer, ARRAY
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy_utils import URLType
from ..database import Base
from db.models.users import User


class Beat(Base):
    __tablename__ = 'beats'

    title = Column(String, index=True)
    genre = Column(String, index=True)
    artwork = Column(URLType, nullable=True)
    user_id = Column(ForeignKey("user_account.id"))
    user: Mapped['User'] = relationship(back_populates='user_beats')
    id = Column(Integer, primary_key=True, index=True)
