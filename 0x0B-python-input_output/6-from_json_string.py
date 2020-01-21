#!/usr/bin/python3
"""
from json string module
"""
import json


def from_json_string(my_str):
    """ Function that returns an object (Python data structure)
        represented by a JSON string

    Args:
        my_str: string.
    """
    return json.loads(my_str)
