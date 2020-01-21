#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename) as file:
        if nb_lines < 1 or nb_lines >= sum([1 for l in file]):
            [print(lines, end='') for lines in file]
        else:
            [print(file.readline(), end='') for i in range(nb_lines)]
