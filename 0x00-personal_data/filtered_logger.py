#!/usr/bin/env python3
""" 0. Regex-ing: filter_datum
    1. Log formatter: logging
    2. Create logger: get_logger
    3. Connect to secure database - get_db
"""

import re
from typing import List
import logging
import mysql.connector
from os import getenv


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Description: Regex-ing - Write a function called filter_datum that
                     returns the log message obfuscated:

        Arguments:
            fields: a list of strings representing all fields to obfuscate
            redaction: a string representing by what the field will be
                       obfuscated
            message: a string representing the log line
            separator: a string representing by which character is
                       separating all fields in the log line (message)
        The function should use a regex to replace occurrences of certain
        field values.
        filter_datum should be less than 5 lines long and use re.sub to
        perform the substitution with a single regex.
    """

    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator,
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        Description: Update the class to accept a list of strings fields
                     constructor argument. """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Description: Implement a get_logger function that takes no arguments
                     and returns a logging.Logger object.
    """
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False

    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    log.addHandler(sh)

    return log

def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Description: Implement a get_db function that returns a connector to the database 
                     (mysql.connector.connection.MySQLConnection object). """
    connection_db = mysql.connector.connection.MySQLConnection(
        username = getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password = getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host = getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database = getenv('PERSONAL_DATA_DB_NAME')
    )

    return connection_db
