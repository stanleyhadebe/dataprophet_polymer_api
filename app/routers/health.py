# app/routers/health.py

from fastapi import APIRouter, Depends
from ..database import get_db

router = APIRouter(tags=["Health"])

@router.get("/health_check")
def health_check(db=Depends(get_db)):
    return {"status": "ok"}
