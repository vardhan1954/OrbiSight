# Store Intelligence System - Design

## Overview

This system processes CCTV footage and converts raw video streams into business intelligence metrics for retail stores.

The pipeline performs:

1. Person Detection
2. Multi-Object Tracking
3. Event Generation
4. Metrics Computation
5. API Exposure

---

## Architecture

Video Input
    ↓
YOLOv8 Person Detection
    ↓
ByteTrack Multi-Object Tracking
    ↓
Event Generator
    ↓
events.json
    ↓
Metrics Engine
    ↓
FastAPI Endpoints
    ↓
Dashboard / Consumers

---

## Components

### Detection Layer

YOLOv8 is used to detect persons from CCTV footage.

### Tracking Layer

ByteTrack assigns persistent IDs to detected individuals.

This prevents double-counting and enables visitor tracking.

### Event Layer

Tracking events are converted into structured business events.

Example:

```json
{
  "person_id": "track_17",
  "event_type": "entry",
  "timestamp": "2026-06-02T12:00:00"
}
```

### Metrics Layer

Business KPIs are computed from generated events:

- Entries
- Exits
- Occupancy
- Conversion Rate

### API Layer

FastAPI exposes analytics endpoints.

Endpoints:

- /process
- /metrics
- /funnel
- /anomalies
- /occupancy
- /aisles

---

## Event Flow

Detection
→ Tracking
→ Event Generation
→ Metric Calculation
→ API Response

---

## Scalability

The architecture separates:

- Detection
- Event Processing
- Analytics

allowing future integration with Kafka, databases, and streaming pipelines.