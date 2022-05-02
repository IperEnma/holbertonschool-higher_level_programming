#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    one = (0, 0)
    two = (0, 0)
    if len(tuple_a) == 0:
        one = 0, 0
    elif len(tuple_a) == 1:
        one = tuple_a[0], 0
    else:
        one = tuple_a[0], tuple_a[1]

    if len(tuple_b) == 0:
        two = 0, 0
    elif len(tuple_b) == 1:
        two = tuple_b[0], 0
    else:
        two = tuple_b[0], tuple_b[1]

    return (one[0] + two[0], one[1] + two[1])
