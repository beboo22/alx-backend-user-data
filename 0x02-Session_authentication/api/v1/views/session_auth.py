#!/usr/bin/env python3
"""
Session authentication route handlers
"""
from api.v1.views import app_views
from models.user import User
from flask import jsonify, request
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """create session_login"""
    from api.v1.app import auth
    user_email = request.form.get("email")
    user_password = request.form.get("password")

    if user_email == "" or user_email is None:
        return jsonify({ "error": "email missing" }), 400

    if user_password == "" or user_password is None:
        return jsonify({ "error": "password missing" }), 400

    user = User.search({"email":user_email})
    if not user:
        return jsonify({ "error": "no user found for this email" }), 404

    user = User.search({"email":user_email})[0]
    if user.is_valid_password(user_password) is False:
        return jsonify({ "error": "wrong password" }), 401
    SessionID = auth.create_session(user.id)
    res = jsonify(user.to_json())
    cookieName = os.getenv("SESSION_NAME")
    res.set_cookie(cookieName, SessionID)
    return res
