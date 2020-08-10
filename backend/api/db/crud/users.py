from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
from passlib.context import CryptContext

from .. import models, schemas
from ...actions import auth

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"

### Users
def get_user(db: Session, username: str):
    return db.query(models.users.User).filter(models.users.User.username == username).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.users.User).filter(models.users.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.users.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.users.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, user: schemas.UserLogin):
    current_user = get_user(db, user.username)
    if not current_user:
        return None
    if not auth.verify_password(user.password, current_user.hashed_password):
        return None
    return current_user