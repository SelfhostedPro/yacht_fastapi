from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import make_transient

from ..db import models, schemas
from ..db.models import containers
from ..db.database import SessionLocal, engine
from .. import actions

import docker
from datetime import datetime
import urllib.request
import json

containers.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def index():
    return actions.get_apps()

@router.get("/{app_name}")
def get_container_details(app_name):
    return actions.get_app(app_name=app_name)

@router.get("/{app_name}/processes", response_model=schemas.Processes)
def get_container_processes(app_name):
    return actions.get_app_processes(app_name=app_name)

@router.get("/{app_name}/logs", response_model=schemas.AppLogs)
def get_container_logs(app_name):
    return actions.get_app_logs(app_name=app_name)

@router.get("/{app_name}/{action}")
def container_actions(app_name,action):
    return actions.app_action(app_name,action)

@router.post("/deploy", response_model=schemas.DeployLogs)
def deploy_app(template: schemas.DeployForm):
    return actions.deploy_app(template=template)