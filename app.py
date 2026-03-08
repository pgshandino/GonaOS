from flask import Flask, render_template
from api.api_routes import api
from dashboards.live_routes import live
from dashboards.analytics_routes import analytics
from utils.scheduler import start_logger
import threading

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

app.register_blueprint(api)
app.register_blueprint(live)
app.register_blueprint(analytics)

def start_background_logger():
    t = threading.Thread(target=start_logger)
    t.daemon = True
    t.start()

if __name__ == "__main__":
    start_background_logger()
    app.run(host="0.0.0.0", port=5000, debug=True)