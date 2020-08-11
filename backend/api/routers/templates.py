from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session
from datetime import datetime

from ..db import crud, schemas
from ..db.models import containers
from ..db.database import SessionLocal, engine
from ..utils import get_db

containers.Base.metadata.create_all(bind=engine)



router = APIRouter()

@router.get("/", response_model=List[schemas.TemplateBase])
def index(db: Session = Depends(get_db)):
    templates = crud.get_templates(db=db)
    return templates

@router.get("/{id}", response_model=schemas.TemplateItems)
def show(id: int, db: Session = Depends(get_db)):
    template = crud.get_template(db=db, id=id)
    return template

@router.delete("/{id}", response_model=List[schemas.TemplateBase])
def delete(id: int, db: Session = Depends(get_db)):
    return crud.delete_template(db=db, template_id=id)

@router.post("/", response_model=schemas.TemplateBase)
def add_template(template: schemas.TemplateBase, db: Session = Depends(get_db)):
    existing_template = crud.get_template(db=db, url=template.url)
    if existing_template:
        raise HTTPException(status_code=400, detail="Template already in Database.")
    return crud.add_template(db=db, template=template)

@router.get("/{id}/refresh", response_model=schemas.TemplateBase)
def refresh_template(id: int, db: Session = Depends(get_db)):
    return crud.refresh_template(db=db, template_id=id)

@router.get("/settings/variables", response_model=List[schemas.TemplateVariables])
def read_template_variables(db: Session = Depends(get_db)):
    return crud.read_template_variables(db=db)

@router.post("/settings/variables", response_model=List[schemas.TemplateVariables])
def set_template_variables(new_variables: List[schemas.TemplateVariables],db: Session = Depends(get_db)):
    return crud.set_template_variables(new_variables=new_variables, db=db)

@router.get("/app/{id}", response_model=schemas.TemplateItem)
def read_app_template(id: int, db: Session = Depends(get_db)):
    return crud.read_app_template(db=db, app_id=id)