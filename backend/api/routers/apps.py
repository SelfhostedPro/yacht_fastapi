from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..db.models import containers
from ..db.database import SessionLocal, engine

containers.Base.metadata.create_all(bind=engine)


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()