import random
from datetime import datetime, timezone

def generate_dynamic_data():
    return {
        "router_id": "R1",
        "hostname": "TJ2100N-14B GPON ONT",
        "ip_address": "192.168.1.1",
        "uptime": f"{random.randint(10, 100)} days, "
                  f"{random.randint(1, 23)} hours, "
                  f"{random.randint(1, 59)} minutes",
        "cpu_usage": random.randint(10, 100),
        "memory_utilization": random.randint(30, 100),
        "bandwidth_usage": {
            "download": random.randint(100, 500),
            "upload": random.randint(20, 100),
        },
        "latency": random.randint(5, 50),
        "packet_loss": round(random.uniform(0.1, 2.0), 2),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "thresholds": {
            "cpu": 75,
            "memory": 75,
            "interface_errors": 5,
            "latency": 100,
            "packet_loss": 2,
        },
    }
