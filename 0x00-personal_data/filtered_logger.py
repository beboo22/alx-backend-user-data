#!/usr/bin/env python3
"""
filter_datum
"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str):
    """ The function should use
    a regex to replace occurrences
    of certain field values."""
    for x in fields:
        message = re.sub(f'{x}=.*?{separator}',
                         f'{x}={redaction}{separator}', message)
    return message
