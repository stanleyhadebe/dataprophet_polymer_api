# app/routers/reactor.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..auth import verify_token
from ..polymer_logic import react_polymer

router = APIRouter(tags=["Reactor"])

@router.get("/reactor")
def reactor(
    start: str,
    end: str,
    db: Session = Depends(get_db),
    user=Depends(verify_token)
):
    # gather polymers → concatenate → run reaction
    pass
