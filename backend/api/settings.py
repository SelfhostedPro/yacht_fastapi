import os
import secrets
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Yacht API"
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(16))
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'pass')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@yacht.local')
    ACCESS_TOKEN_EXPIRES = os.environ.get('ACCESS_TOKEN_EXPIRES', 15)
    REFRESH_TOKEN_EXPIRES = os.environ.get('REFRESH_TOKEN_EXPIRES', 1)
