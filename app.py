from flask import Flask, Response, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["path", "method"])
LATENCY = Histogram("http_request_duration_seconds", "Request latency in seconds", ["path"])
HARVEST_KG = Counter("harvest_total_kg_total", "Total harvested kilograms", ["crop"])

@app.get("/health")
def health():
    REQUESTS.labels(path="/health", method="GET").inc()
    return jsonify(ok=True)

@app.get("/plants")
def plants():
    start = time.time()
    REQUESTS.labels(path="/plants", method="GET").inc()

    crops = ["tomato", "wheat", "corn"]
    crop = random.choice(crops)

    HARVEST_KG.labels(crop=crop).inc(random.randint(1, 5))

    time.sleep(0.05)
    LATENCY.labels(path="/plants").observe(time.time() - start)

    app.logger.info("plants endpoint called, crop=%s", crop)
    return jsonify(plants=crops, selected=crop)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
