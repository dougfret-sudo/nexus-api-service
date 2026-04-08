# Yellow Iron Nexus API (v1.0.0)
**High-Performance Backend Service for Industrial Asset Distribution**

## 🏗️ Overview
The **Nexus API** is the distribution layer of the Yellow Iron Arbitrage ecosystem. It transforms raw SQL data collected by the Nexus Scraper into a structured, professional REST API. This service allows private buyers and internal systems to query high-ROI "Yellow Iron" deals (Track Hoes, Dozers, Graders) through a secure and documented gateway.

### ⚙️ System Logic
- **[Data Modeling]**: Uses Pydantic for strict schema validation, ensuring all machine "Particulars" (Hours, Price, Serial Prefixes) are formatted correctly.
- **[Query Engine]**: Provides dynamic filtering capabilities, allowing users to isolate deals by price ceiling, machine category, or regional location.
- **[Auto-Documentation]**: Self-documents via OpenAPI/Swagger, providing an interactive UI for developers to test endpoints in real-time.

---

## 🛠️ Technical Stack
- **Framework**: Python 3.x (FastAPI)
- **Data Source**: SQLite3 (Shared with Nexus Scraper Engine)
- **Validation**: Pydantic v2
- **Server**: Uvicorn (ASGI)

---

## 🚀 Quick Start (Development Mode)

### 1. Installation
```bash
pip install fastapi uvicorn pydantic python-dotenv
