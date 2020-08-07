from typing import List, Optional
from pydantic import BaseModel, Json

class TemplateItem(BaseModel):
    type: int
    title: str
    name: str
    platform: int
    description: int
    logo: str
    image: str
    notes: str
    categories: Json
    restart_poplicy: Json
    ports: Json
    volumes: Json
    env: Json
    sysctls: Json
    cap_add: Json
    
    class Config:
        orm_mode = True

class TemplateBase(BaseModel):
    title: str
    url: str
    items: List[TemplateItem] = []

    class Config:
        orm_mode = True

class TemplateVariables(BaseModel):
    variable: str
    replacement: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True