#!/usr/bin/python3
"""
to json string module
"""
import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object (string)
    
    Args:
        my_obj: object.
    
    Return:
        JSON representation of an object
    """
    return json.dumps(my_obj)
