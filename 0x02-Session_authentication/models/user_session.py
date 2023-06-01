#!/usr/bin/env python3
""" Define UserSession Model. """

from models.base import Base


class UserSession(Base):
    """ User session Class. """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize class instance. """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
