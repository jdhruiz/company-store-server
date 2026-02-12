from flask import Blueprint, jsonify
from db import get_connection

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/reset", methods=["POST"])
def reset_database():
    conn = get_connection()
    cur = conn.cursor()

    # Order matters due to foreign keys
    cur.execute("TRUNCATE order_items RESTART IDENTITY CASCADE;")
    cur.execute("TRUNCATE orders RESTART IDENTITY CASCADE;")
    cur.execute("TRUNCATE items RESTART IDENTITY CASCADE;")
    cur.execute("TRUNCATE cadets RESTART IDENTITY CASCADE;")

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Database reset successful"}), 200
