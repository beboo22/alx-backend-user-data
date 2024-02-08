#!/usr/bin/env python3
"""
filter_datum
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Generate a random salt and hash the password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Use bcrypt to check if the provid password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
