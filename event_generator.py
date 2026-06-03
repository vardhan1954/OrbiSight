from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    event_id: str
    person_id: str
    session_id: str
    event_type: str
    timestamp: datetime