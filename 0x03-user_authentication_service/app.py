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
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        res = jsonify({"email": email, "message": "logged in"})
        res.set_cookie("session_id", session_id)
        return res
    else:
        abort(401)


@app.route('/sessions', methods=["DELETE"])
def logout() -> Union[str, None]:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    session_id = request.cookies.get("session_id")
    find_user = AUTH.get_user_from_session_id(session_id)
    if find_user is None:
        abort(403)
    AUTH.destroy_session(find_user.id)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
