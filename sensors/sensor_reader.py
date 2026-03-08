import random
from datetime import datetime

# Replace with real GPIO reads
def read_sensors():
    return {
        "temperature": round(random.uniform(24,32),2),
        "humidity": round(random.uniform(60,80),2),
        "rain_detected": random.choice([0,1]),
        "soil_dry": random.choice([0,1]),
        "recorded_at": datetime.utcnow()
    }