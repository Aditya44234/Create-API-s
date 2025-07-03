from flask import Flask
from app.routes.users import user_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/register": {"origins": "*"}})
    app.register_blueprint(user_bp)
    return app

