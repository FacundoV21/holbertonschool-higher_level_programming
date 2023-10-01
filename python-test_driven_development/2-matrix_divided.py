#!/usr/bin/python3
"""
    Division function, which divides a amtrix of integers, the tests for this
    function are located on the tests folder

"""


def matrix_divided(matrix, div):
    """
    Divides each element of the matrix by div
    """
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')

    if all(not isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')

    size = len(matrix[0])
    for row in matrix:
        for column in row:
            if not isinstance(column, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
        if len(row) != size:
            raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    result = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return result
