import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException
from .routers import apps, templates
import uuid

from .db import models
from .db.database import SessionLocal
from .settings import Settings

from .auth import fastapi_users, get_auth_router, cookie_authentication, database, users, UserCreate, get_password_hash, user_db_model, user_db

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
    get_auth_router(cookie_authentication),
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    templates.router,
    prefix="/templates",
    tags=["templates"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@app.on_event("startup")
async def startup():
    await database.connect()
    users_exist = await database.fetch_all(query=users.select())
    if users_exist:
        print(users_exist)
    else:
        print("no users")
        ### This is where I'm having trouble
        # user_create_model
        # hashed_password = get_password_hash(settings.ADMIN_PASSWORD)
        # base_user = user_db_model(
        #     id = uuid.uuid4(),
        #     email= settings.ADMIN_EMAIL,
        #     password= settings.ADMIN_PASSWORD,
        #     hashed_password= hashed_password,
        #     is_active= True,
        #     is_superuser= True
        # )
        # db_user = user_db_model(
        #     **base_user.create_update_dict(), id = uuid.uuid4()
        # )
        # await user_db.create(db_user)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
