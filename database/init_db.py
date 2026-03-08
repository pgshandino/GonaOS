import sys
from pathlib import Path

# Add parent directory to path so we can import config
sys.path.insert(0, str(Path(__file__).parent.parent))

from db import get_connection

def init():
    conn = get_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS sensor_readings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperature REAL,
        humidity REAL,
        rain_detected INTEGER,
        soil_dry INTEGER,
        recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init()