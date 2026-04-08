import os
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Yellow Iron Nexus API",
    description="Professional API for industrial asset distribution and ROI tracking.",
    version="1.0.0"
)

# 1. Data Model (The "Particulars")
class MachineListing(BaseModel):
    category: str
    make_model: str
    listed_price: float
    machine_hours: Optional[int] = None
    source_url: str
    is_deal: bool

# 2. Database Connection
def get_db():
    # Looks for 'nexus.db' path in your .env file
    db_path = os.getenv("DATABASE_URL", "nexus.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def home():
    return {"status": "Online", "system": "Yellow Iron Nexus API", "version": "1.0.0"}

@app.get("/deals", response_model=List[MachineListing])
def get_deals():
    """Fetches all high-ROI deals from the local Nexus database."""
    try:
        conn = get_db()
        cursor = conn.cursor()
        # Query matching your scraper's output
        query = "SELECT category, make_model, listed_price, machine_hours, source_url, is_deal FROM machinery_inventory WHERE is_deal = 1"
        rows = cursor.execute(query).fetchall()
        conn.close()
        
        # Convert SQL rows to Python dictionaries for FastAPI
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database Error: {str(e)}")
