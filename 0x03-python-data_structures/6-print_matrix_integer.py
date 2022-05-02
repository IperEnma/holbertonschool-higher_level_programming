#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (not(matrix == [[]])):
        for x in matrix:
            count = 0
            for y in x:
                if (count != 2):
                    print((y), end=' ')
                else:
                    print((y), end='')
                count = count + 1
            print()
    else:
        print()
