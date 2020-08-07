from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_

from . import models, schemas
from passlib.context import CryptContext
from .utils import conv_ports2dict, conv_sysctls2dict



import urllib.request
import json

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
    db.refresh(db.user)
    return db_user

### Templates
def get_templates(db: Session, skip: int = 0):
    return db.query(models.containers.Template).offset(skip).all()

def get_template_items(db: Session, template_id: int):
    return db.query(models.containers.Template).get_or_404(template_id)

def add_template(db: Session, template: schemas.TemplateBase, TemplateItem: schemas.TemplateItem):
    try:
    # Opens the JSON and iterate over the content.
        with urllib.request.urlopen(template.url) as file:
            for entry in json.load(file):

                ports = conv_ports2dict(entry.get('ports', []))
                sysctls = conv_sysctls2dict(entry.get('sysctls', []))

                # Optional use classmethod from_dict
                template_content = TemplateItem(
                    type = int(entry['type']),
                    title = entry['title'],
                    platform = entry['platform'],
                    description = entry.get('description', ''),
                    name = entry.get('name', entry['title'].lower()),
                    logo = entry.get('logo', ''), # default logo here!
                    image = entry.get('image', ''),
                    notes = entry.get('note', ''),
                    categories = entry.get('categories', ''),
                    restart_policy = entry.get('restart_policy'),
                    ports = ports,
                    volumes = entry.get('volumes', []),
                    env = entry.get('env', []),
                    sysctls = sysctls,
                    cap_add = entry.get('cap_add', [])
                )
                template.items.append(template_content)
    except (OSError, TypeError, ValueError) as err:
        # Optional handle KeyError here too.
        print('data request failed', err)
        raise

    try:
        db.add(template)
        db.commit()
    except IntegrityError as err:
        # TODO raises IntegrityError on duplicates (uniqueness)
        #       status
        db.rollback()
        pass

    return template