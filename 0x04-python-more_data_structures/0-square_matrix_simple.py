#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtx = [i[:] for i in matrix]
    idx = 0
    for row in mtx:
        for val in row:
            row[idx] = val ** 2
            idx += 1
        idx = 0
    return mtx
