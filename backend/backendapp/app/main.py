from app.db.session import engine
from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db import base_class


base_class.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)