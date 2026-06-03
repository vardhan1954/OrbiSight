import json
import uuid
from datetime import datetime


EVENT_FILE = "data/events.json"


def save_event(
    person_id,
    session_id,
    event_type
):
    event = {
        "event_id": str(uuid.uuid4()),
        "person_id": person_id,
        "session_id": session_id,
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        with open(EVENT_FILE, "r") as f:
            events = json.load(f)
    except:
        events = []

    events.append(event)

    with open(EVENT_FILE, "w") as f:
        json.dump(events, f, indent=2)