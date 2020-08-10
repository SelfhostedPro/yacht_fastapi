from fastapi import APIRouter, Depends, HTTPException
from datetime import timedelta

from sqlalchemy.orm import Session

from ..db import crud, schemas
from ..db.models import users
from ..db.database import SessionLocal, engine
from ..settings import Settings

from ..actions import auth

users.Base.metadata.create_all(bind=engine)
settings = Settings()

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def initial_user():
    if not crud.get_users(db=SessionLocal()):
        print("no users")
        settings = Settings()
        user = schemas.UserCreate
        user.username = settings.ADMIN_EMAIL
        user.password = settings.ADMIN_PASSWORD
        crud.create_user(db=SessionLocal(), user=user)

initial_user()

@router.post("/login", response_model=schemas.Token)
def login(form: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES)
    refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRES)
    return {
        "access_token": auth.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "refresh_token": auth.create_refresh_token(
            user.id, expires_delta=refresh_token_expires
        ),
        "token_type": "bearer",
    }

# @router.post("/create", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     existing_templates = crud.get_user(db=db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)

# @router.post