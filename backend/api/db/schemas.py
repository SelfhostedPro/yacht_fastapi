from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Json
### TEMPLATES BEGIN ###
### TEMPLATE ITEMS ###
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

### APPS ###
class PortsSchema(BaseModel):
    cport: int
    hport: int
    proto: str

class VolumesSchema(BaseModel):
    container: str
    bind: str

class EnvSchema(BaseModel):
    label: str
    default: str
    name: Optional[str]
    description: Optional[str]

class SysctlsSchema(BaseModel):
    name: str
    value: str

class DeployForm(BaseModel):
    name: str
    image: str
    restart_policy: str
    notes: Optional[str]
    ports: Optional[List[PortsSchema]]
    volumes: Optional[List[VolumesSchema]]
    env: Optional[List[EnvSchema]]
    sysctls: Optional[List[SysctlsSchema]]
    cap_add: Optional[str]
# LOGS #
class DeployLogs(BaseModel):
    logs: str
class AppLogs(BaseModel):
    logs: str

# Processes #
class Processes(BaseModel):
    Processes: List[List[str]]
    Titles: List[str]
### USERS ###
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
