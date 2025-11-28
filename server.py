from flask import Flask, jsonify, Response, stream_with_context
from flask_cors import CORS
import time
import json
from dynamic_data import generate_dynamic_data

app = Flask(__name__)
CORS(app)

# --------------------------------------------------------
# Normal API → returns fresh data on each request
# --------------------------------------------------------
@app.route("/api/network-data")
def get_network_data():
    data = generate_dynamic_data()
    return jsonify(data)

# --------------------------------------------------------
# Server-Sent Events → streams new data every 3 sec
# --------------------------------------------------------
@app.route("/api/live-network-data")
def stream_network_data():

    def generate():
        while True:
            data = generate_dynamic_data()
            yield f"data: {json.dumps(data)}\n\n"
            time.sleep(3)

    headers = {
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no"
    }

    return Response(stream_with_context(generate()),
                    mimetype="text/event-stream",
                    headers=headers)

# --------------------------------------------------------
# Run Server
# --------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, threaded=True)
