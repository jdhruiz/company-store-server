from flask import Blueprint, jsonify, request
from db import get_connection
from utils import query_db

cadets_bp = Blueprint("cadets", __name__)

@cadets_bp.route("/", methods=["GET"])
def get_cadets():
    data = query_db("SELECT * FROM cadets;")
    return jsonify(data)

@cadets_bp.route("/", methods=["POST"])
def add_cadet():
    data = request.json

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO cadets (first_name, last_name, company, class_year)
        VALUES (%s, %s, %s, %s)
    """, (
        data["first_name"],
        data["last_name"],
        data["company"],
        data["class_year"]
    ))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Cadet added"}, 201
