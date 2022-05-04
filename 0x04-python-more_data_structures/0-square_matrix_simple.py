#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    value = 0
    for x in range(len(matrix)):
        new.append([])
        for y in range(len(matrix[x])):
            value = matrix[x][y] ** 2
            new[x].append(value)
    return new
