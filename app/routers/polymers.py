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
    try:
        for polymer_data in polymers:
            polymer = Polymer(
                timestamp=polymer_data.timestamp,
                polymer=polymer_data.polymer
            )
            db.add(polymer)
        db.commit()
        return {"status": "success", "count": len(polymers)}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/polymers", response_model=list[PolymerOut])
def get_polymers(
    start: str,
    end: str,
    db: Session = Depends(get_db),
    user=Depends(verify_token)
):
    from datetime import datetime
    start_dt = datetime.fromisoformat(start)
    end_dt = datetime.fromisoformat(end)
    polymers = db.query(Polymer).filter(
        Polymer.timestamp >= start_dt,
        Polymer.timestamp <= end_dt
    ).all()
    return polymers
