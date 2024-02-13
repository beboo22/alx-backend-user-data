#!/usr/bin/env python3
"""Template for all authentication system"""

from api.v1.auth.auth import Auth
from typing import List, TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """BasicAuth class inherits from Auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts base64 encoded authorization header"""
        if (authorization_header is None or
                not isinstance(authorization_header, str) or
                authorization_header[:6] != "Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Extracts base64 encoded authorization header"""
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            base64.b64decode(base64_authorization_header)
        except ValueError:
            return None
        return base64.b64decode(base64_authorization_header).decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Extracts base64 encoded authorization header"""
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str) or
                ":" not in decoded_base64_authorization_header):
            return None, None
        else:
            s = decoded_base64_authorization_header.split(":")
            return (s[0], s[1])

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """Extracts base64 encoded authorization header"""
        if (
          user_email is None
          or user_pwd is None
          or not isinstance(user_email, str)
          or not isinstance(user_pwd, str)
        ):
            return None

        x = User()
        search_result = x.search({'email': user_email})

        if search_result is None or\
           not isinstance(search_result, list)\
           or len(search_result) == 0:
            return None

        user_object = search_result[0]

        if user_object.is_valid_password(user_pwd):
            return user_object
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        Authorization_header = self.authorization_header(request)
        if  not Authorization_header:
            return None
        
        extract_authorization_header = self.extract_base64_authorization_header(Authorization_header)
        decode_authorization_header = self.decode_base64_authorization_header(extract_authorization_header)
        extract_credentials = self.extract_user_credentials(decode_authorization_header)
        user_email = extract_credentials[0]
        user_pwd = extract_credentials[1]
        extract_credentials = self.user_object_from_credentials(user_email, user_pwd)
        return extract_credentials


