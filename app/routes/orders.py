from flask import Blueprint, request, jsonify
from db import get_connection

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["POST"])
def create_order():
    data = request.json

    conn = get_connection()
    cur = conn.cursor()

    # Insert order
    cur.execute("""
        INSERT INTO orders (cadet_id)
        VALUES (%s)
        RETURNING id
    """, (data["cadet_id"],))

    order_id = cur.fetchone()[0]

    # Insert order items
    for item in data["items"]:
        cur.execute("""
            INSERT INTO order_items (order_id, item_id, quantity)
            VALUES (%s, %s, %s)
        """, (order_id, item["item_id"], item["quantity"]))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "message": "Order created",
        "order_id": order_id
    }), 201
