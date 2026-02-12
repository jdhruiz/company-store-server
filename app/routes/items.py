from flask import Blueprint, jsonify, request
from db import get_connection
from utils import query_db
import pandas as pd

items_bp = Blueprint("items", __name__)

@items_bp.route("/", methods=["GET"])
def get_items():
    data = query_db("SELECT * FROM items;")
    return jsonify(data)

@items_bp.route("/", methods=["POST"])
def add_item():
    data = request.json

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO items (name, price, in_stock_qty)
        VALUES (%s, %s, %s)
    """, (data["name"], data["price"], data["in_stock_qty"]))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Item added"}, 201

@items_bp.route("/upload", methods=["POST"])
def upload_items():
    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400

    file = request.files["file"]
    df = pd.read_csv(file)

    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO items (name, price, in_stock_qty)
            VALUES (%s, %s, %s)
        """, (row["name"], row["price"], row["in_stock_qty"]))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Items uploaded successfully"}
