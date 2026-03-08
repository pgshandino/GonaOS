from flask import Blueprint, render_template
from services.analytics_service import daily_summary

analytics = Blueprint("analytics", __name__)

@analytics.route("/dashboard")
def dashboard():
    trends = daily_summary()
    return render_template("dashboard.html", trends=trends)