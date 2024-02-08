#!/usr/bin/env python3
"""
filter_datum
"""
from typing import List
import re
import logging
import mysql.connector
import os
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    db_userName = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_userPASS = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_userHOST = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_Name = os.getenv("PERSONAL_DATA_DB_NAME")
    conn = mysql.connector.connection.MySQLConnection(
        user=db_userName,
        password=db_userPASS,
        host=db_userHOST,
        database=db_Name
    )
    return conn


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str) -> str:
    """ Returns a log message obfuscated """
    for x in fields:
        message = re.sub(f'{x}=.*?{separator}',
                         f'{x}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """ returns a logging.Logger object."""
    Logger = logging.LogRecord("user_data", logging.INFO)
    Logger.propagate = False
    Stream_Handler = logging.StreamHandler()
    Stream_Handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(Stream_Handler)
    return Logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """  Formatter func
        """
        record.msg = filter_datum(self.fields,
                                  self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def main():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    for row in cursor:
        print(row[0])
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
