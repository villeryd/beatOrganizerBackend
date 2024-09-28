from fastapi import APIRouter, Depends, HTTPException
from libraries.beats.schemas import Beat

from sqlalchemy import Boolean, Column, String, ForeignKey, Integer, ARRAY
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy_utils import URLType, EmailType
from ..database import Base
from typing import List, Optional
from db.models.beats import Beat


class UserBase(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = Column(EmailType, unique=True, index=True)
    hashed_password = Column(String)
    user_beats: Mapped[List["Beat"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"
