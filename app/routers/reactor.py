# app/routers/reactor.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..auth import verify_token
from ..polymer_logic import react_polymer
from ..models import Polymer

router = APIRouter(tags=["Reactor"])

@router.get("/reactor")
def reactor(
    start: str,
    end: str,
    db: Session = Depends(get_db),
    user=Depends(verify_token)
):
    from datetime import datetime
    from ..schemas import ReactorResult
    
    start_dt = datetime.fromisoformat(start)
    end_dt = datetime.fromisoformat(end)
    
    polymers = db.query(Polymer).filter(
        Polymer.timestamp >= start_dt,
        Polymer.timestamp <= end_dt
    ).all()
    
    chain = "".join([p.polymer for p in polymers])
    result, reactions = react_polymer(chain)
    
    return ReactorResult(
        start_timestamp=start_dt,
        end_timestamp=end_dt,
        reaction_count=reactions,
        result=result
    )
