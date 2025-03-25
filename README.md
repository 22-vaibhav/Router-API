# 🚀 Router Network Monitoring API  

This API provides **real-time** and **current network data** for monitoring routers dynamically.  
The data is continuously updated **every 3 seconds** and can be fetched via REST API or **real-time streaming**.  

---

## 📡 **Live API Endpoints**  

### 🔴 **1. Fetch Real-Time Network Data (Streaming)**  
> **URL:** [https://router-api-qga7.onrender.com/api/live-network-data](https://router-api-qga7.onrender.com/api/live-network-data)  
> **Description:**  
> - Provides **live updates** on network performance.  
> - Uses **Server-Sent Events (SSE)** for continuous updates.  
> - No need to refresh—data updates automatically.  

**📌 Example (JavaScript Fetch - Live Updates)**  
```javascript
const eventSource = new EventSource("https://router-api-qga7.onrender.com/api/live-network-data");

eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log("Live Update:", data);
};
```

### 🔴 **2. Fetch Current Network Data (Latest Snapshot)**  
> **URL:** [https://router-api-qga7.onrender.com/api/network-data](https://router-api-qga7.onrender.com/api/network-data)  
> **Description:**  
> - Returns the **latest network statistics** as a JSON response.  
> - Best for applications that need **periodic polling** instead of live streaming.  

**📌 Example (JavaScript Fetch - Current Data)**  
```javascript
fetch("https://router-api-qga7.onrender.com/api/network-data")
  .then(response => response.json())
  .then(data => console.log("Latest Data:", data))
  .catch(error => console.error("Error fetching data:", error));
};
```

## ⚙️ **How API works**

### **1. Live Data Streaming (SSE):**
> - ```/api/live-network-data``` sends updates continuously to connected clients.

### **2. Fetch-on-Request API:**
> - ```/api/network-data``` provides the latest snapshot of router statistics.

## 📌 **Example API Response**  
```json
{
    "router_id": "R1",
    "hostname": "TJxxxN-xxB GPON ONT",
    "ip_address": "192.168.1.1",
    "uptime": "52 days, 10 hours, 23 minutes",
    "cpu_usage": 45,
    "memory_utilization": 65,
    "bandwidth_usage": {
        "download": 310,
        "upload": 85
    },
    "latency": 12,
    "packet_loss": 1.3,
    "timestamp": "2025-03-25T05:32:44.953172+00:00"
}
```

## 🎯 **How to Use This API**  

### 📌 **For Web & Frontend Applications**  
> - Use JavaScript ```fetch()``` to request data.
> - Use **SSE (Server-Sent Events)** for real-time updates.

### 📌 **For Python Applications** 

```python
import requests

API_URL = "https://router-api-qga7.onrender.com/api/network-data"

response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()
    print("Latest Network Data:", data)
else:
    print("Failed to fetch data")
```
