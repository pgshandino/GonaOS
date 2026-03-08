from flask import Blueprint, render_template
from sensors.sensor_reader import read_sensors

live = Blueprint("live", __name__)

@live.route("/live")
def live_dashboard():
    data = read_sensors()
    return render_template("live.html", data=data)