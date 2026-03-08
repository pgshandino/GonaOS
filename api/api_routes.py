from flask import Blueprint, request, jsonify
from database.db import get_connection

api = Blueprint("api", __name__)

@api.route("/api/readings")
def readings():
    start = request.args.get("start")
    end = request.args.get("end")

    query = "SELECT * FROM sensor_readings WHERE 1=1"
    params = []

    if start:
        query += " AND recorded_at >= ?"
        params.append(start)

    if end:
        query += " AND recorded_at <= ?"
        params.append(end)

    conn = get_connection()
    rows = conn.execute(query, params)
    data = [dict(row) for row in rows]
    conn.close()

    return jsonify(data)