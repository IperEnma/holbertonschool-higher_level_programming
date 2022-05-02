#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for x in matrix:
            for y in x:
                if (y != x[-1]):
                    print((y), end=' ')
                else:
                    print((y), end='')
            print()
