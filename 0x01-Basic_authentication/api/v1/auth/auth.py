#!/usr/bin/env python3
"""  template for all authentication system
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manage API authentication methods
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Return boolean """
        return False

    def authorization_header(self, request=None) -> str:
        """ Return boolean """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return boolean """
        return None
