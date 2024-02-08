#!/usr/bin/env python3
"""
filter_datum
"""
from typing import List
import re
import logging
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
