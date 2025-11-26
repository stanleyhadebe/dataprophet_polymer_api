# app/routers/polymers.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Polymer
from ..schemas import PolymerIn, PolymerOut
from ..auth import verify_token

router = APIRouter(tags=["Polymers"])

@router.post("/polymers")
def ingest_polymers(
    polymers: list[PolymerIn],
    db: Session = Depends(get_db),
    user=Depends(verify_token)
):
    # insert logic here
    pass

@router.get("/polymers", response_model=list[PolymerOut])
def get_polymers(
    start: str,
    end: str,
    db: Session = Depends(get_db),
    user=Depends(verify_token)
):
    # retrieval logic here
    pass
