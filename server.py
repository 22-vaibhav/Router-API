from flask import Flask, jsonify, Response, stream_with_context
import json
import time
import threading
from dynamic_data import generate_dynamic_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

JSON_FILE = "network_data.json"


# ------------------ API Endpoint to Get Latest JSON Data ------------------
@app.route("/api/network-data", methods=["GET"])
def get_network_data():
    """Returns the latest JSON data."""
    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "Failed to read JSON", "details": str(e)}), 500


# ------------------ Real-Time Streaming API (Server-Sent Events) ------------------
@app.route("/api/live-network-data")
def stream_network_data():
    """Streams updated JSON data in real-time."""

    def generate():
        while True:
            try:
                with open(JSON_FILE, "r") as file:
                    data = json.load(file)
                yield f"data: {json.dumps(data)}\n\n"
            except Exception as e:
                yield f"data: {{'error': 'Failed to read JSON', 'details': '{str(e)}'}}\n\n"
            time.sleep(3)

    return Response(stream_with_context(generate()), mimetype="text/event-stream")


# ------------------ Function to Continuously Update JSON File ------------------
def update_json_continuously():
    """Runs in a separate thread to update network_data.json continuously."""
    while True:
        generate_dynamic_data()
        time.sleep(3)


# Start background thread for dynamic data updates
threading.Thread(target=update_json_continuously, daemon=True).start()


# ------------------ Run Flask API Server ------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, threaded=True)
