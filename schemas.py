from pydantic import BaseModel
from datetime import datetime

class PolymerIn(BaseModel):
    timestamp: datetime
    polymer: str

class PolymerOut(PolymerIn):
    pass

class ReactorResult(BaseModel):
    start_timestamp: datetime
    end_timestamp: datetime
    reaction_count: int
    result: str
