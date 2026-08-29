"""Deliberately vulnerable Flask app for SAST/DAST demos. DO NOT DEPLOY."""
from flask import Flask, request, jsonify
import sqlite3, jwt, os

app = Flask(__name__)
SECRET = "hardcoded-secret-123"  # SAST flag: hardcoded credential

@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    pwd  = request.form["pwd"]
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    # SAST flag: SQL injection via string formatting
    cur.execute(f"SELECT * FROM users WHERE name='{user}' AND pwd='{pwd}'")
    if cur.fetchone():
        token = jwt.encode({"user": user}, SECRET, algorithm="HS256")
        return {"token": token}
    return {"error": "invalid"}, 401

@app.route("/admin")
def admin():
    # SAST flag: no authorization check (IDOR/authz missing)
    return {"flag": "s3cr3t"}
