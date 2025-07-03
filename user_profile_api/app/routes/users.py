from flask import Blueprint, jsonify, request, Response
from datetime import datetime
import csv
from fpdf import FPDF
from io import BytesIO
from flask_cors import CORS


user_bp = Blueprint('user_bp', __name__)
CORS(user_bp)  # 👈 Apply CORS to this blueprint directly



entries = []

@user_bp.route("/")
def home():
    return jsonify(
        {
            "id": 1,
            "name": "Aditya",
            "email": "aditya@example.com",
            "role": "developer",
            "message": "Exploring APIs!",
            "timestamp": "2025-07-01 21:05:33"
        }
    )

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    id = data.get('id')
    name = data.get('name')
    email = data.get('email')
    role = data.get('role')
    message = data.get('message')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not all([id, name, email, role, message]):
        return jsonify({
            "error": "All fields are required ",
            "fields": "[ id,name,email,role,message ]"
        })

    entry = {
        "id": id,
        "name": name,
        "email": email,
        "role": role,
        "message": message,
        "timestamp": timestamp,
    }

    entries.append(entry)
    return jsonify({
        "Entry": entry
    })

@user_bp.route("/users")
def users():
    return jsonify({
        "Entries": entries[::-1]
    })

@user_bp.route("/user/<name>")
def user_Name(name):
    for entry in entries:
        if entry['name'].lower() == name.lower():
            return jsonify({
                "User_entry": entry
            })
    return jsonify({
        "error": "Invalid Username"
    })

@user_bp.route("/count")
def count():
    count = len(entries)
    return jsonify({
        "Number of user": count
    })

@user_bp.route("/latest")
def latest():
    latest = entries[-1]
    return jsonify({
        "Latest Entry": latest
    })

@user_bp.route("/stats")
def stats():
    role_counts = {}
    for entry in entries:
        role = entry['role']
        role_counts[role] = role_counts.get(role, 0) + 1
    return jsonify({"role_stats": role_counts})


from app.utils import export
