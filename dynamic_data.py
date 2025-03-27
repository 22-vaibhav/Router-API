import json
import random
import time
from datetime import datetime, timezone

JSON_FILE = "network_data.json"


def generate_dynamic_data():
    """Generates random network data and updates the JSON file."""
    data = {
        "router_id": "R1",
        "hostname": "TJ2100N-14B GPON ONT",
        "ip_address": "192.168.1.1",
        "uptime": f"{random.randint(10, 100)} days, {random.randint(1, 23)} hours, {random.randint(1, 59)} minutes",
        "cpu_usage": random.randint(10, 100),
        "memory_utilization": random.randint(30, 100),
        "bandwidth_usage": {
            "download": random.randint(100, 500),  # Mbps
            "upload": random.randint(20, 100),  # Mbps
        },
        "latency": random.randint(5, 50),  # ms
        "packet_loss": round(random.uniform(0.1, 2.0), 2),  # percentage
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "thresholds": {
            "cpu": 75,
            "memory": 75,
            "interface_errors": 5,
            "latency": 100,
            "packet_loss": 2,
        },
    }

    # Overwriting `network_data.json` with new data
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return data


# 🔄 Run in a loop to continuously update the JSON file
if __name__ == "__main__":
    while True:
        generate_dynamic_data()  # Updates `network_data.json`
        print("✅ Updated network_data.json at", datetime.now().strftime("%H:%M:%S"))
        time.sleep(3)  # Updates every 3 seconds
