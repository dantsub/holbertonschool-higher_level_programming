#!/usr/bin/python3
""" Function divide a matrix """


def matrix_divided(matrix, div):
    """ Divide a matrix.
    """
    # Validate is a matrix and long of rows and the cols are a int
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(col, int) or isinstance(col, float))
                    for col in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    # validate div is a number
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    # validate the len or size the matrix's rows are len same
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # validate if div is 0
    if div == 0:
        raise ZeroDivisionError('division by zero')
    # return new matrix with the divide.
    return [list(map(lambda a: round(a / div, 2), row)) for row in matrix]
