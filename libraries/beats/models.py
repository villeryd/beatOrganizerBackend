from fastapi import APIRouter, Depends, HTTPException
from .schemas import Beat

from sqlalchemy import Boolean, Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=ForeignKey, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    beats = relationship('Beat', back_populates='owner')


class Beat(Base):
    __tablename__ = 'beats'

    id = Column(Integer, primary_key=ForeignKey, index=True)
    title = Column(String, index=True)
    tags = Column(list[String], index=True)
    genre = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates='beats')
