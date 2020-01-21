#!/usr/bin/python3
"""
Read file module
"""


def read_file(filename=""):
    """ Function thats read a file """
    with open(filename, encoding='utf-8') as file:
        [print(line, end='') for line in file]
