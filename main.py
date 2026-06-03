from fastapi import FastAPI
from app.services.metrics import calculate_metrics
from app.services.metrics import calculate_funnel
from app.pipeline.processor import process_video

app = FastAPI(
    title="Store Intelligence System",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "service": "store-intelligence"
    }

@app.get("/metrics")
def metrics():
    return calculate_metrics()

@app.get("/funnel")
def funnel():
    return calculate_funnel()

@app.get("/anomalies")
def anomalies():

    metrics = calculate_metrics()

    anomalies = []

    if metrics["occupancy"] > 100:
        anomalies.append(
            {
                "type": "occupancy_spike",
                "message": "Store occupancy unusually high"
            }
        )

    if metrics["entries"] == 0:
        anomalies.append(
            {
                "type": "no_activity",
                "message": "No visitors detected"
            }
        )

    return anomalies

@app.get("/process")
def process():

    result = process_video("data/sample.mp4")

    return result

@app.get("/occupancy")
def occupancy():

    metrics = calculate_metrics()

    return {
        "occupancy": metrics["occupancy"]
    }

@app.get("/aisles")
def aisles():

    return {
        "aisle_1": 12,
        "aisle_2": 8,
        "aisle_3": 5
    }