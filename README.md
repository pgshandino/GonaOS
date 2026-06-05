# GonaOS - Agricultural IoT Sensor Monitoring System

## 📋 About

**GonaOS** is a comprehensive agricultural IoT monitoring system designed to track environmental and soil conditions in real-time. Built on the Raspberry Pi platform, it integrates multiple sensors to collect data on temperature, humidity, rainfall, and soil moisture. The system provides a Flask-based web dashboard for live monitoring, data analytics, and historical data retrieval, making it ideal for precision agriculture, weather monitoring, and automated irrigation systems.

### Project Overview
GonaOS enables farmers and researchers to:
- Monitor real-time environmental conditions (temperature, humidity)
- Detect rainfall events for irrigation management
- Track soil moisture levels for water conservation
- Visualize historical data trends through interactive dashboards
- Access sensor data via RESTful APIs for integration with external systems

---

## 🔧 GPIO Pin Configuration

| Sensor/Component | GPIO Pin | BCM Pin | Physical Pin | Purpose |
|------------------|----------|---------|--------------|---------|
| DHT22 (Temp/Humidity) | GPIO4 | 4 | 7 | Temperature & Humidity readings |
| Rain Sensor | GPIO17 | 17 | 11 | Rainfall detection |
| Soil Moisture Sensor | GPIO27 | 27 | 13 | Soil moisture level detection |

**Pin Setup Notes:**
- All pins use BCM (Broadcom) numbering mode
- Rain and Soil sensors are configured with internal pull-up resistors
- DHT22 uses the Adafruit CircuitPython library for reliable data reading

---

## 📦 Installation & Setup

### Prerequisites
- Raspberry Pi (3B+ or later recommended)
- Python 3.7 or higher
- pip (Python package manager)
- Internet connection for weather API
- GPIO access (requires root/sudo privileges for some operations)

### Hardware Setup

1. **Mount Sensors to Raspberry Pi:**
   - Connect DHT22 to GPIO4 (Pin 7, Ground, 3.3V)
   - Connect Rain Sensor to GPIO17 (Pin 11, Ground, 3.3V)
   - Connect Soil Moisture Sensor to GPIO27 (Pin 13, Ground, 3.3V)
   - Ensure proper ground connections to Raspberry Pi GND pins

2. **Enable GPIO Interface:**
   ```bash
   sudo raspi-config
   # Navigate to Interface Options → GPIO → Enable
   ```

### Software Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/pgshandino/GonaOS.git
   cd GonaOS
   ```

2. **Create Virtual Environment (Recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Application:**
   - Edit `config.py` and update:
     - `OPENWEATHER_API_KEY`: Get your free API key from [OpenWeatherMap](https://openweathermap.org/api)
     - `CITY`: Set your city for weather data
     - `DB_PATH`: Adjust database location if needed (default: `database/gona_v1.db`)

   ```python
   # config.py
   DB_PATH = "database/gona_v1.db"
   CITY = "Abuja"  # Change to your location
   OPENWEATHER_API_KEY = "YOUR_API_KEY"  # Insert your OpenWeather API key
   ```

5. **Initialize Database:**
   ```bash
   python3 -c "from database.db import init_db; init_db()"
   ```

6. **Run the Application:**
   ```bash
   python3 app.py
   ```
   - The Flask server will start on `http://0.0.0.0:5000`
   - Access the dashboard at `http://localhost:5000` (or your Raspberry Pi's IP address)

---

## 📋 Requirements

### System Requirements
- **Operating System:** Raspberry Pi OS (Bookworm or newer recommended)
- **RAM:** Minimum 1GB (2GB+ recommended)
- **Storage:** Minimum 2GB available space
- **Python Version:** 3.7+

### Python Dependencies
All required packages are listed in `requirements.txt`:

```
flask              # Web framework for dashboard and APIs
RPi.GPIO           # GPIO library for Raspberry Pi pin control
adafruit-circuitpython-dht  # DHT sensor library
requests           # HTTP library for API calls
```

### Network Requirements
- Active internet connection for weather API calls to OpenWeatherMap
- Local network access for web dashboard

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Flask (Python micro web framework)
- **Database:** SQLite3 (lightweight, file-based database)
- **GPIO Control:** RPi.GPIO (Raspberry Pi GPIO library)
- **Sensor Libraries:** 
  - Adafruit CircuitPython DHT22
  - Built-in GPIO libraries

### Frontend
- **Templates:** Jinja2 (Flask template engine)
- **HTML/CSS/JavaScript:** For interactive dashboards
- **Real-time Updates:** AJAX/Fetch API

### APIs & External Services
- **OpenWeatherMap API:** For weather data integration
- **RESTful API:** Custom endpoints for sensor data retrieval

### System Architecture
- **Single-threaded + Background Tasks:** Daemon threads for continuous logging
- **Data Persistence:** SQLite database for historical records
- **Modular Design:** Separated concerns (sensors, services, dashboards, APIs)

---

## 📁 Project Structure

```
GonaOS/
├── app.py                          # Main Flask application entry point
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
│
├── sensors/
│   └── sensor_reader.py           # Sensor reading logic (DHT22, Rain, Soil)
│
├── api/
│   └── api_routes.py              # REST API endpoints for sensor data
│
├── services/
│   ├── data_logger.py             # Database logging service
│   ├── weather_service.py         # OpenWeather API integration
│   └── analytics_service.py       # Data analytics and calculations
│
├── dashboards/
│   ├── live_routes.py             # Live dashboard routes
│   └── analytics_routes.py        # Analytics dashboard routes
│
├── database/
│   ├── gona_v1.db                 # SQLite database (auto-created)
│   └── db.py                      # Database connection management
│
├── utils/
│   └── scheduler.py               # Background task scheduling
│
├── templates/
│   └── index.html                 # Main HTML template
│
└── .git/                          # Git repository
```

---

## 🚀 Features

### Real-time Monitoring
- ✅ Live temperature and humidity readings (DHT22)
- ✅ Instant rainfall detection alerts
- ✅ Soil moisture status indicators
- ✅ Weather integration with external API

### Data Management
- ✅ Persistent data storage in SQLite
- ✅ Historical data queries with date range filtering
- ✅ Automated data logging with timestamps
- ✅ Data cleanup and maintenance utilities

### Web Dashboard
- ✅ Responsive live monitoring dashboard
- ✅ Analytics and trend visualization
- ✅ Interactive data filtering
- ✅ Real-time updates via AJAX

### API Endpoints
- ✅ `/api/readings` - Query sensor readings with time filters
- ✅ Live data endpoints for dashboard
- ✅ Analytics endpoints for trend analysis

---

## 🔌 API Usage

### Get Sensor Readings
```bash
# All readings
curl http://localhost:5000/api/readings

# With date range filter
curl "http://localhost:5000/api/readings?start=2024-01-01&end=2024-01-31"
```

**Response Format:**
```json
[
  {
    "id": 1,
    "temperature": 28.5,
    "humidity": 65.2,
    "rain_detected": false,
    "soil_dry": false,
    "recorded_at": "2024-01-15T14:32:00"
  }
]
```

---

## 📊 Database Schema

### sensor_readings Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER PRIMARY KEY | Unique reading identifier |
| temperature | REAL | Temperature in Celsius |
| humidity | REAL | Humidity percentage (0-100) |
| rain_detected | BOOLEAN | Rain detection status |
| soil_dry | BOOLEAN | Soil moisture status |
| recorded_at | TIMESTAMP | UTC timestamp of reading |

---

## 🔐 Security Considerations

1. **API Key Management:**
   - Store `OPENWEATHER_API_KEY` securely, never commit to version control
   - Use environment variables or `.env` files in production
   - Regenerate keys periodically

2. **GPIO Access:**
   - GPIO operations may require root privileges
   - Use dedicated user accounts with minimal permissions
   - Be cautious with GPIO manipulation to avoid hardware damage

3. **Database Access:**
   - SQLite database is file-based; secure file permissions appropriately
   - Backup database regularly

4. **Network Security:**
   - Run behind a firewall/reverse proxy in production
   - Implement authentication if exposing to public networks
   - Use HTTPS for sensitive deployments

---

## 🐛 Troubleshooting

### Sensor Reading Issues
- **DHT22 returning None:** Check wiring, ensure proper voltage (3.3V), try increasing delay between reads
- **GPIO errors:** Verify GPIO mode is set to BCM, check pin numbers
- **Permission denied:** Run with `sudo` or add user to GPIO group

### Database Issues
- **Database locked:** Ensure only one instance of the application is running
- **No data in database:** Check that `data_logger.py` is functioning and recording

### API Issues
- **Weather data not loading:** Verify API key is correct and active
- **Network timeout:** Check internet connection and firewall rules

---

## 📝 Usage Examples

### Monitor Temperature Trends
Access the analytics dashboard at `http://localhost:5000/analytics` to view temperature trends over time.

### Check for Rain Events
The live dashboard displays real-time rain detection. Query the API:
```bash
curl "http://localhost:5000/api/readings?start=2024-01-01" | grep rain_detected
```

### Export Data
Download sensor readings in JSON format via the API for external analysis.

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is open source. Please refer to the LICENSE file for details.

---

## 📞 Support & Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [pgshandino](https://github.com/pgshandino)

---

## 🗺️ Roadmap

- [ ] Mobile app for remote monitoring
- [ ] Machine learning for predictive alerts
- [ ] Multi-location support
- [ ] Email/SMS notifications
- [ ] Historical data export (CSV, Excel)
- [ ] Docker containerization

---

**Last Updated:** June 2024
**Version:** 1.0
