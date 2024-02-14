#!/usr/bin/env python3
"""Template for all authentication system"""

from api.v1.auth.auth import Auth
from typing import List, TypeVar
from models.user import User
import base64


class SessionAuth(Auth):
    """BasicAuth class inherits from Auth class"""
    pass
