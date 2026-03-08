from database.db import get_connection

def daily_summary():
    conn = get_connection()
    rows = conn.execute(
        '''
        SELECT DATE(recorded_at) as day,
               AVG(temperature) as avg_temp,
               AVG(humidity) as avg_humidity,
               SUM(rain_detected) as rain_events
        FROM sensor_readings
        GROUP BY day
        ORDER BY day DESC
        LIMIT 30
        '''
    )
    data = [dict(row) for row in rows]
    conn.close()
    return data