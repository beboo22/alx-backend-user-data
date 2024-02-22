#!/usr/bin/env python3
"""
Main file
"""
from flask import Flask, jsonify, request, abort
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.exc import InvalidRequestError
from typing import Union

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


@app.route('/sessions', methods=["POST"])
def login() -> Union[str, None]:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie("session_id", session_id)
    return res


@app.route('/sessions', methods=["DELETE"])
def logout() -> Union[str, None]:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    session_id = request.cookies.get("session_id", None)
    find_user = AUTH.get_user_from_session_id(session_id)
    if find_user is None or session_id is None:
        abort(403)
    AUTH.destroy_session(find_user.id)
    return redirect("/")


@app.route('/profile', methods=["GET"])
def profile() -> Union[str, None]:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    session_id = request.cookies.get("session_id", None)
    find_user = AUTH.get_user_from_session_id(session_id)
    if find_user is None or session_id is None:
        abort(403)
    return jsonify({"email": find_user.email})


@app.route('/reset_password', methods=["POST"])
def get_reset_password_token() -> Union[str, None]:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "reset_token": reset_token}), 200


@app.route('/reset_password', methods=["PUT"])
def update_password() -> Union[str, None]:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
