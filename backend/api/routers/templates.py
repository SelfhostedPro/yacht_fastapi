from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session
from datetime import datetime

from ..db import crud, schemas
from ..db.models import containers
from ..db.database import SessionLocal, engine

containers.Base.metadata.create_all(bind=engine)


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.TemplateBase])
def index(db: Session = Depends(get_db)):
    templates = crud.get_templates(db=db)
    return templates

@router.get("/{id}", response_model=List[schemas.TemplateItem])
def show(id: int, db: Session = Depends(get_db)):
    template_items = crud.get_template_items(db=db, template_id=id)
    return template_items

@router.delete("/{id}", response_model=List[schemas.TemplateBase])
def delete(id: int, db: Session = Depends(get_db)):
    return crud.delete_template(db=db, template_id=id)

@router.post("/add", response_model=schemas.TemplateBase)
def add_template(template: schemas.TemplateBase, db: Session = Depends(get_db)):
    existing_template = crud.get_template(db=db, url=template.url)
    if existing_template:
        raise HTTPException(status_code=400, detail="Template already in Database.")
    return crud.add_template(db=db, template=template)

@router.get("/{id}/refresh", response_model=schemas.TemplateRefresh)
def refresh_template(id: int, db: Session = Depends(get_db)):
    return crud.refresh_template(db=db, template_id=id)