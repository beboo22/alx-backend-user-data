#!/usr/bin/env python3
"""
Main file
"""
import bcrypt
from user import Base, User
from db import DB


def _hash_password(password: str) -> bytes:
    """Hash the password using bcrypt"""
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except BaseException:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
