#!/usr/bin/env python3
"""  template for all authentication system
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    Manage API authentication methods
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if authorization_header is None\
        or not isinstance(authorization_header, str):
            return None
        if authorization_header[:6] == "Basic ":
            return authorization_header[6:]
        else:
            return None
