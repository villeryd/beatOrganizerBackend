from fastapi import APIRouter, Depends, HTTPException
from libraries.beats.schemas import Beat

from sqlalchemy import Boolean, Column, String, ForeignKey, Integer, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType
from ..database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # beats = relationship('Beats', back_populates='user')


class Beat(Base):
    __tablename__ = 'beats'

    title = Column(String, index=True)
    genre = Column(String, index=True)
    artwork = Column(URLType, nullable=True)
    # owner_id = Column(Integer, ForeignKey('user.id'))
    # owner = relationship("User", back_populates='beats')
    id = Column(Integer, primary_key=True, index=True)
