#!/usr/bin/python3
"""
number of lines module
"""


def number_of_lines(filename=""):
    """ Function thats return number of lines of filename """
    with open(filename) as file:
        return sum([1 for line in file])
