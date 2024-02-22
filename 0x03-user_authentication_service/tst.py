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
print(bcrypt.checkpw(password, hashed_password))
