#!/usr/bin/env python3
"""
Main file
"""
import bcrypt
import uuid
from typing import Union
from user import Base, User
from db import DB
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """Hash the password using bcrypt"""
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password


def _generate_uuid() -> str:
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        try:
            find_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        password = password.encode("utf-8")
        hashed_password = find_user.hashed_password
        if bcrypt.checkpw(password, hashed_password):
            return True
        return False

    def create_session(self, email: str):
        try:
            find_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(find_user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        if session_id is None:
            return None
        try:
            find_user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return find_user
