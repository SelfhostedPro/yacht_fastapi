from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, session
from ..auth import User

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# def get_users():
#     return session.query(User).count()

# def initial_user():
#     if not get_users():
#         print("no users")
#         settings = Settings()
#         user = schemas.UserCreate
#         user.username = settings.ADMIN_EMAIL
#         user.password = settings.ADMIN_PASSWORD
#         crud.create_user(db=SessionLocal(), user=user)

# initial_user()