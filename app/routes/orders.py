from flask import Blueprint, request, jsonify
from db import get_connection
from utils import query_db

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["GET"])
def get_orders():
    data = query_db("SELECT * FROM orders;")
    return jsonify(data)

@orders_bp.route("/", methods=["POST"])
def create_order():
    data = request.json

    conn = get_connection()
    cur = conn.cursor()

