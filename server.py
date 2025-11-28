from flask import Flask, jsonify, Response, stream_with_context
from flask_cors import CORS
import json
import time
import threading
from dynamic_data import generate_dynamic_data

app = Flask(__name__)
CORS(app)

# SINGLE SHARED MEMORY DATA → super fast
latest_data = {}

# --------------------------------------------------------
# BACKGROUND THREAD: updates in-memory data only
# --------------------------------------------------------
def update_data_continuously():
    global latest_data
    while True:
        latest_data = generate_dynamic_data()  # NO FILE WRITING
        time.sleep(3)

threading.Thread(target=update_data_continuously, daemon=True).start()

# --------------------------------------------------------
# Normal API Endpoint
# --------------------------------------------------------
@app.route("/api/network-data")
def get_network_data():
    return jsonify(latest_data)

# --------------------------------------------------------
# Server-Sent Events (Live Streaming)
# --------------------------------------------------------
@app.route("/api/live-network-data")
def live_stream():

    def generate():
        while True:
            yield f"data: {json.dumps(latest_data)}\n\n"
            time.sleep(3)

    return Response(stream_with_context(generate()), mimetype="text/event-stream")

# --------------------------------------------------------
# Run Server
# --------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, threaded=True)
