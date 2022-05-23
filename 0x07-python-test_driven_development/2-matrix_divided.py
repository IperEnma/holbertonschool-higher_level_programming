#!/usr/bin/python3
"""module divide elements matrix"""


def matrix_divided(matrix, div):
    """function"""
    count = 0

    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for x in matrix:
        if type(x) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    count = len(matrix[0])
    for x in matrix:
            if len(x) != count:
                raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
         raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)),matrix))
    return new
