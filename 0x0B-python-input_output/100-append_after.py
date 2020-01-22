#!/usr/bin/python3
"""
append after module
"""


def append_after(filename="", search_string="", new_string=""):
    """ Description
    Args:
        filename (str):
        search_string (str):
        new_string (str):
    """
    with open(filename, mode='r+', encoding='utf-8') as file:
        [file.readline() for l in file if l not in search_string]
        file.write(new_string)
