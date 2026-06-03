from collections import defaultdict

from ultralytics import YOLO
from app.services.event_generator import save_event

# Better accuracy than yolov8n while still being practical
model = YOLO("yolov8s.pt") #preferable for better accuracy, but can be switched to yolov8n for faster processing

"""
we can use either :
model = YOLO("yolov8m.pt")
model = YOLO("yolov8n.pt")
"""
# Track must survive N frames before being considered valid
MIN_TRACK_AGE = 5


def process_video(video_path):

    visitor_ids = set()

    # Track lifecycle
    track_frames = defaultdict(int)

    # Where a track first appeared
    first_positions = {}

    results = model.track(
        source=video_path,
        persist=True,
        tracker="bytetrack.yaml",
        verbose=False,
        stream=True
    )

    for result in results:

        if result.boxes.id is None:
            continue

        height, width = result.orig_shape

        # Entrance approximation:
        # left 15% OR right 15% of frame
        margin = int(width * 0.15)

        boxes = result.boxes

        track_ids = boxes.id.int().cpu().tolist()

        for i, track_id in enumerate(track_ids):

            x1, y1, x2, y2 = boxes.xyxy[i].tolist()

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            # Track age
            track_frames[track_id] += 1

            # Remember where track first appeared
            if track_id not in first_positions:
                first_positions[track_id] = (
                    center_x,
                    center_y
                )

            # Ignore unstable tracks
            if track_frames[track_id] < MIN_TRACK_AGE:
                continue

            # Already counted
            if track_id in visitor_ids:
                continue

            start_x, start_y = first_positions[track_id]

            # New visitor must originate near frame boundary
            originates_near_boundary = (
                start_x < margin
                or
                start_x > (width - margin)
            )

            if originates_near_boundary:

                save_event(
                    person_id=f"track_{track_id}",
                    session_id=f"session_{track_id}",
                    event_type="entry"
                )

                visitor_ids.add(track_id)

    return {
        "unique_visitors": len(visitor_ids)
    }