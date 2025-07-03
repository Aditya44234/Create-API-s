import os
from flask import Flask, jsonify, request, Response
from .users import user_bp  # Import your blueprint
from dotenv import load_dotenv

load_dotenv()  # 👈 Loads values from .env automatically

def create_app():
    app = Flask(__name__)

    # 🛡️ Use SECRET_KEY from .env file
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback_if_missing")

    app.register_blueprint(user_bp)

    return app

    