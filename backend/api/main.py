from fastapi import Depends, FastAPI, Header, HTTPException
from .routers import auth, apps, templates

from .db import models
from .db.database import engine

app = FastAPI()

app.include_router(
    apps.router,
    prefix="/apps",
    tags=["apps"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    templates.router,
    prefix="/templates",
    tags=["templates"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)