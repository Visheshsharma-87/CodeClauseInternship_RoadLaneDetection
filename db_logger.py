import sqlite3
import os
from datetime import datetime

# Auto-create DB folder if not present
DB_PATH = os.path.join("database", "lane_logs.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def init_db():
    """Create the lane_logs table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS lane_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Ensure DB is initialized once when module loads
init_db()

def log_lane_detection(status):
    """
    Log lane detection result to SQLite database.
    status: 1 (Lanes Detected) or 0 (No Lanes Found)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_str = "Lanes Detected" if status == 1 else "No Lanes Found"

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO lane_logs (timestamp, status) VALUES (?, ?)", (timestamp, status_str))
        conn.commit()
        conn.close()
    except Exception as e:
        print("Logging Error:", e)
