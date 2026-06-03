# Engineering Decisions and Tradeoffs

## Objective

The goal of this project was to build an end-to-end Store Intelligence System that transforms CCTV footage into business metrics such as visitor counts, occupancy, and conversion insights.

The focus was on creating a working system with clear event generation and analytics rather than maximizing model accuracy.

---

## Why YOLOv8

YOLOv8 was selected because:

- Fast deployment
- Good real-time performance
- Strong person detection capability
- Easy integration with Python

Alternative options such as DeepStream and custom detectors were considered but would significantly increase system complexity and deployment effort.

Tradeoff:

- Slightly lower optimization than DeepStream pipelines
- Faster development and easier maintainability

---

## Why ByteTrack

The challenge requires visitor tracking and session-level analytics.

ByteTrack was selected because:

- Stable multi-object tracking
- Works directly with YOLO detections
- Easy integration with Ultralytics

Benefits:

- Reduces double counting
- Enables visitor-level event generation

---

## Why Event-Based Architecture

Instead of directly computing metrics from detections, the system generates structured events.

Example:

```json
{
  "person_id": "track_17",
  "event_type": "entry"
}
```

Advantages:

- Decouples analytics from detection
- Easier debugging
- Supports future streaming architectures
- Simplifies KPI generation

---

## Why FastAPI

FastAPI was selected because:

- Lightweight
- High performance
- Automatic API documentation
- Simple deployment

The API layer exposes business metrics independently of the vision pipeline.

---

## Why JSON Event Storage

For the scope of this challenge, JSON-based storage was used.

Advantages:

- Simple implementation
- Easy inspection during evaluation
- No database dependency

Future versions can replace this layer with:

- PostgreSQL
- Kafka
- Event streaming systems

without changing the analytics layer.

---

## Assumptions

The following assumptions were made:

- CCTV camera placement remains fixed
- Person detection is the primary signal
- Each tracking ID represents a unique visitor session
- Video quality is sufficient for person detection

---

## Known Limitations

- No re-identification across cameras
- Basic anomaly detection logic
- Limited zone-level analytics
- No distributed event streaming

---

## Future Improvements

- Multi-camera tracking
- Kafka event streaming
- Database-backed analytics
- Shelf interaction detection
- Basket detection
- Real-time dashboard updates
- Advanced anomaly detection