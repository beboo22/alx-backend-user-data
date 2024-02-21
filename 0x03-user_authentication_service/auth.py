#!/usr/bin/env python3
"""
Main file
"""
import bcrypt


def _hash_password(password: str):
    """Memoized session object
    """
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password
