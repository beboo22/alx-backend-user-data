# import sqlalchemy

# print(sqlalchemy.__version__)
#!/usr/bin/env python3
"""
Main file
"""
import bcrypt

password = b"beboo"
salt = bcrypt.gensalt()

hashed_password = bcrypt.hashpw(password, salt)

print(hashed_password)
# def _hash_password(password:str):
#     return password.encode("utf-8")
