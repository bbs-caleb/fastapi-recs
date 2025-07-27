from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.v1.router import api_router
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)
app.include_router(api_router, prefix="/api/v1")

