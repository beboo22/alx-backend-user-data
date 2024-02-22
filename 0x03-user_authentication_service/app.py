#!/usr/bin/env python3
"""
Main file
"""
from flask import Flask, jsonify, request
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.exc import InvalidRequestError

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"])
def index() -> str:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"])
def register_users() -> str:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
