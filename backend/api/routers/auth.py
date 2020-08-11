# from fastapi import APIRouter, Depends, HTTPException, Response
# from datetime import timedelta

# from sqlalchemy.orm import Session

# from ..db import crud, schemas
# from ..db.models import users
# from ..db.database import SessionLocal, engine
# from ..settings import Settings

# from ..actions import auth

# users.Base.metadata.create_all(bind=engine)
# settings = Settings()

# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

def initial_user():
    if not crud.get_users(db=SessionLocal()):
        print("no users")
        settings = Settings()
        user = schemas.UserCreate
        user.username = settings.ADMIN_EMAIL
        user.password = settings.ADMIN_PASSWORD
        crud.create_user(db=SessionLocal(), user=user)

initial_user()
