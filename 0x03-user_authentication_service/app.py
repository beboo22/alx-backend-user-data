#!/usr/bin/env python3
"""
Main file
"""
from flask import flask


app = flask(__name__)


@app.route('/', method="GET")
def index() -> str:
    """GET /
    Return:
        - JSON payload containing a welcome message.
    """
    return jsonify({"message": "Bienvenue"})
