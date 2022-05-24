#!/usr/bin/python3
"""module prints a square"""


def print_square(size):
    """function prints a square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    
    if size == 0:
        return 
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
