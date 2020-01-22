#!/usr/bin/python3
"""
append after module
"""


def append_after(filename="", search_string="", new_string=""):
    """ Insert text after each line containing a given string in a file
    Args:
        filename (str): filename
        search_string (str): string to search for within the file
        new_string (str): string will be insert into file
    """
    with open(filename, mode='r+', encoding='utf-8') as file:
        string = [l + new_string if search_string in l else l for l in file]
        string = "".join(string)
        file.seek(0)
        file.write(string)
