#!/usr/bin/python3
"""
load from json file module
"""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file”

    Args:
        filename (str): filename.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
