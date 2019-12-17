#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 0
    for row in matrix:
        for val in row:
            if (idx == 0):
                print ('{}'.format(val), end='')
            else:
                print ('{:2}'.format(val), end='')
            idx += 1
        idx = 0
        print()
