from flask import Flask
from routes.cadets import cadets_bp
from routes.items import items_bp
from routes.orders import orders_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(cadets_bp, url_prefix="/cadets")
    app.register_blueprint(items_bp, url_prefix="/items")
    app.register_blueprint(orders_bp, url_prefix="/orders")

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
