#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 0
    for row in matrix:
        for val in row:
            if (idx == 0):
                print('{:d}'.format(val), end='')
            else:
                print('{:2d}'.format(val), end='')
            idx += 1
        idx = 0
        print()
