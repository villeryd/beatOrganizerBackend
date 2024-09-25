from fastapi import APIRouter, Depends, HTTPException
from libraries.beats.schemas import Beat

from sqlalchemy import Boolean, Column, String, ForeignKey, Integer, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType, EmailType
from ..database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(EmailType, unique=True, index=True)
    hashed_password = Column(String)
    beats = relationship('beats', back_populates='user')
