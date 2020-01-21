#!/usr/bin/python3
""" write file module """


def write_file(filename="", text=""):
    """ Function that writes a string to
        a text file (UTF8) and returns the
        number of characters written
        
    Args:
        filename (str): filename
        text (str): text. 
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        return file.write(text)
