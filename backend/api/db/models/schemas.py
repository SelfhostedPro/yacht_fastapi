from typing import List, Optional
from pydantic import BaseModel, Json

class TemplateBase(BaseModel):
    title: str
    url: str

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
    template_id: int

class TemplateVariables(BaseModel):
    variable: str
    replacement: str

    class Config:
        orm_mode = True