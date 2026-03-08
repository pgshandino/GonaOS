import requests
from config import OPENWEATHER_API_KEY, CITY

def get_forecast():
    if OPENWEATHER_API_KEY == "YOUR_API_KEY":
        return []
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric"
    r = requests.get(url)
    return r.json().get("list", [])