#!/usr/bin/python3
"""
save to json file module
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
        using a JSON representation

    Args:
        my_obj (object): an object.
        filename (str): filename.
    Return:
        Nothing
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
