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
        if path is None:
            return True

        if path[-1] != '/':
            path = path + '/'

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path not in excluded_paths:
            return True

        if path in excluded_paths:
            return False

        x = "/api/v1/status/"
        if (path == "/api/v1/status"
           or path == "/api/v1/status/") and x in excluded_paths:
            return False

        return False

    def authorization_header(self, request=None) -> str:
        """ Return boolean """
        if request is None or "Authorization" or request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return boolean """
        return None
