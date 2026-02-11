from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="db",  # IMPORTANT: service name from docker-compose
        database="storedb",
        user="storeuser",
        password="storepass"
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/cadets")
def get_cadets():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cadets;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
