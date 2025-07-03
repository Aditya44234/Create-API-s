from flask import Flask, jsonify, request, Response
from app.routes.users import user_bp
from app import create_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    
