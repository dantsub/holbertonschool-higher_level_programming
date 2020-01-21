#!/usr/bin/python3
"""
read lines module
"""


def read_lines(filename="", nb_lines=0):
    """ Function thats read lines """
    with open(filename, encoding='utf-8') as file:
        if nb_lines < 1 or nb_lines >= sum([1 for l in file]):
            [print(lines, end='') for lines in file]
        else:
            file.seek(0)
            [print(file.readline(), end='') for i in range(nb_lines)]
