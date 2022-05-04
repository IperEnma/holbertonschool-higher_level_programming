#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    count = 0
    for x in matrix:
        count2 = 0
        for y in x:
            new[count][count2] = y * y
            count2 = count2 + 1
        count = count + 1
    return new
