from database.db import get_connection

def save_reading(data):
    conn = get_connection()
    conn.execute(
        '''
        INSERT INTO sensor_readings
        (temperature, humidity, rain_detected, soil_dry, recorded_at)
        VALUES (?, ?, ?, ?, ?)
        ''',
        (
            data["temperature"],
            data["humidity"],
            data["rain_detected"],
            data["soil_dry"],
            data["recorded_at"]
        )
    )
    conn.commit()
    conn.close()