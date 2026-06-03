import json


def load_events():
    with open("data/events.json", "r") as f:
        return json.load(f)


def calculate_metrics():
    events = load_events()

    entries = sum(1 for e in events if e["event_type"] == "entry")
    exits = sum(1 for e in events if e["event_type"] == "exit")

    shelf_visits = sum(
        1 for e in events if e["event_type"] == "shelf_visit"
    )

    occupancy = max(entries - exits, 0)

    conversion_rate = (
        round(shelf_visits / entries, 2)
        if entries > 0
        else 0
    )

    return {
        "entries": entries,
        "exits": exits,
        "occupancy": occupancy,
        "conversion_rate": conversion_rate
    }

def calculate_funnel():
    events = load_events()

    entered = len(
        set(
            e["person_id"]
            for e in events
            if e["event_type"] == "entry"
        )
    )

    shelf = len(
        set(
            e["person_id"]
            for e in events
            if e["event_type"] == "shelf_visit"
        )
    )

    purchased = len(
        set(
            e["person_id"]
            for e in events
            if e["event_type"] == "purchase"
        )
    )

    return {
        "entered": entered,
        "visited_shelf": shelf,
        "checkout": max(purchased, shelf),  # Ensure checkout can't exceed shelf visits
        "purchased": purchased
    }