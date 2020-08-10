import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException
from .routers import auth, apps, templates

from .db.crud import get_user
from .db import models
from .db.database import SessionLocal
from .settings import Settings

app = FastAPI()
settings = Settings()

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

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)