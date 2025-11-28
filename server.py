# server.py
import os
import time
import json
import logging
from flask import Flask, jsonify, Response, stream_with_context
from flask_cors import CORS
from dynamic_data import generate_dynamic_data

# Basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("router-api")

app = Flask(__name__)
CORS(app, supports_credentials=True)

# SSE generator settings
DATA_INTERVAL = 3           # seconds between data messages
HEARTBEAT_INTERVAL = 10     # seconds between heartbeats (ensure <= platform idle limit)

@app.route("/api/network-data")
def get_network_data():
    """Return fresh data on each request (no caching)."""
    data = generate_dynamic_data()
    return jsonify(data)

@app.route("/api/live-network-data")
def live_stream():
    """
    Streams fresh data repeatedly. Sends a data event every DATA_INTERVAL seconds,
    and sends a lightweight SSE comment (heartbeat) every HEARTBEAT_INTERVAL seconds to keep connection alive.
    """

    def generate():
        last_heartbeat = time.time()
        while True:
            # produce fresh data
            data = generate_dynamic_data()
            # send data event
            yield f"data: {json.dumps(data)}\n\n"

            # send heartbeat comment if enough time passed (a colon-line is a valid SSE comment)
            now = time.time()
            if now - last_heartbeat >= HEARTBEAT_INTERVAL:
                yield ":\n\n"
                last_heartbeat = now

            # sleep a short interval and loop - ensures regular data messages
            # We keep DATA_INTERVAL as primary cadence.
            time.sleep(DATA_INTERVAL)

    headers = {
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",   # for nginx/proxies to disable buffering
        "Connection": "keep-alive"
    }

    return Response(stream_with_context(generate()),
                    mimetype="text/event-stream",
                    headers=headers)


if __name__ == "__main__":
    # Use PORT env (Render sets it); fallback to 8000 locally
    port = int(os.environ.get("PORT", 8000))
    # Note: For local dev, flask's built-in server is ok. In production we run via gunicorn.
    app.run(host="0.0.0.0", port=port, debug=False, threaded=True)
