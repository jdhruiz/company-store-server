from flask import Blueprint, jsonify
from utils import query_db

cadets_bp = Blueprint("cadets", __name__)

@cadets_bp.route("/", methods=["GET"])
def get_cadets():
    data = query_db("SELECT * FROM cadets;")
    return jsonify(data)
