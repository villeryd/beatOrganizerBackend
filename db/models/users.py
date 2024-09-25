from fastapi import APIRouter, Depends, HTTPException
from libraries.beats.schemas import Beat

from sqlalchemy import Boolean, Column, String, ForeignKey, Integer, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType, EmailType
from ..database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(ForeignKey('user.id'), primary_key=True, index=True)
    user_name = Column(String, index=True)
    email = Column(EmailType, unique=True, index=True)
    hashed_password = Column(String)
    beats = relationship('beats', back_populates='user.id')
