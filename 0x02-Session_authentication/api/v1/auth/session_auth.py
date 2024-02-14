#!/usr/bin/env python3
"""Template for all authentication system"""

from api.v1.auth.auth import Auth
from typing import List, TypeVar
from models.user import User
import base64
import uuid


class SessionAuth(Auth):
    """BasicAuth class inherits from Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            None
        else:
            SessionID = str(uuid.uuid4())
            self.user_id_by_session_id[SessionID] = user_id
            return SessionID
