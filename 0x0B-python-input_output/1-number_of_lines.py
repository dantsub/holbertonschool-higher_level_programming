#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename) as file:
        return sum([1 for line in file])
