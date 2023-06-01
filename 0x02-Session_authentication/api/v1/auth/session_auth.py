#!/usr/bin/env python3
""" Define SessionAuth class. """

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    pass
