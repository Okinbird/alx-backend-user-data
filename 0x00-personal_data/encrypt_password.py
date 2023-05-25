#!/usr/bin/env python3
"""
   5. Encrypting passwords - hash_password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Description: Implement a hash_password function that expects one string
                     argument name password and returns a salted, hashed
                     password, which is a byte string.

        Use the bcrypt package to perform the hashing (with hashpw).
    """
    pass_encoded = password.encode()
    hashed_pass = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())

    return hashed_pass
