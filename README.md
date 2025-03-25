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
    console.log("🔴 Live Update:", data);
};
