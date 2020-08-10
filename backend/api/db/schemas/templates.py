from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Json

class TemplateItem(BaseModel):
    type: int
    title: str
    name: str
    platform: str
    description: Optional[str]
    logo: Optional[str]
    image: str
    notes: Optional[str]
    categories: Optional[List]
    restart_policy: str
    ports: Optional[List]
    volumes: Optional[List]
    env: Optional[List]
    sysctls: Optional[List]
    cap_add: Optional[List]
    
    class Config:
        orm_mode = True
### TEMPLATE ####
class TemplateBase(BaseModel):
    title: str
    url: str

    class Config:
        orm_mode = True
class TemplateItems(TemplateBase):
    items: List[TemplateItem] = []
class TemplateRefresh(TemplateBase):
    updated_at: datetime
### TEMPLATES END ###

### TEMPLATE VARIABLES ###
class TemplateVariables(BaseModel):
    variable: str
    replacement: str

    class Config:
        orm_mode = True
class ReadTemplateVariables(TemplateVariables):
    id: int