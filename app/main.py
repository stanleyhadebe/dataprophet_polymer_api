# app/main.py

from fastapi import FastAPI
from .database import engine
from . import models
from .routers import health, polymers, reactor

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register routers
app.include_router(health.router)
app.include_router(polymers.router)
app.include_router(reactor.router)
