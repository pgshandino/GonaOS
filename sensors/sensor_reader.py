import board
import adafruit_dht
import RPi.GPIO as GPIO
from datetime import datetime

# =============================
# GPIO CONFIGURATION
# =============================
GPIO.setmode(GPIO.BCM)

DHT_PIN = board.D4          # GPIO4 (Physical Pin 7)
RAIN_PIN = 17               # GPIO17 (Physical Pin 11)
SOIL_PIN = 27               # GPIO27 (Physical Pin 13)

GPIO.setup(RAIN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SOIL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

dht = adafruit_dht.DHT22(DHT_PIN, use_pulseio=False)

# =============================
# SENSOR READ FUNCTION
# =============================
def read_sensors():
    data = {
        "temperature": None,
        "humidity": None,
        "rain_detected": False,
        "soil_dry": False,
        "timestamp": datetime.utcnow().isoformat()
    }

    # --- DHT Reading ---
    try:
        temperature = dht.temperature
        humidity = dht.humidity

        if temperature is not None:
            data["temperature"] = round(temperature, 2)
        if humidity is not None:
            data["humidity"] = round(humidity, 2)

    except RuntimeError:
        # DHT occasionally throws timing errors
        pass

    # --- Digital Sensors ---
    rain_state = GPIO.input(RAIN_PIN)
    soil_state = GPIO.input(SOIL_PIN)

    # Digital modules usually output LOW when triggered
    data["rain_detected"] = (rain_state == 0)
    data["soil_dry"] = (soil_state == 1)

    return data


def cleanup():
    GPIO.cleanup()