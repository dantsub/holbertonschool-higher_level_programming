#!/usr/bin/python3
"""
Pascal triangle module
"""


def pascal_triangle(n):
    """ Represent Pascal's Triangle of size n. """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        tri = pascal[-1]
        one = [1]
        for i in range(len(tri) - 1):
            one.append(tri[i] + tri[i + 1])
        one.append(1)
        pascal.append(one)
    return pascal
