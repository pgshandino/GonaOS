import time
from sensors.sensor_reader import read_sensors
from services.data_logger import save_reading

def start_logger():
    while True:
        data = read_sensors()
        save_reading(data)
        time.sleep(60)