from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    username = Column(String(64),
        nullable=False, unique=True, index=True)
    hashed_password = Column(String(255),
        nullable=False, unique=False, index=False)