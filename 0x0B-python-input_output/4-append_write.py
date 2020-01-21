#!/usr/bin/python3
"""
append write module
"""


def append_write(filename="", text=""):
    """ Function that appends a string at the end of
        a text file (UTF8) and returns the number of
        characters added

    Args:
        filename (str): filename.
        text (str): text to append the file.
    Return:
        Numbers of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
