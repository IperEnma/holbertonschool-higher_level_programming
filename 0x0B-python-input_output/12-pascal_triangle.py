#!/usr/bin/python3
"""module create triangle pascal"""


def pascal_triangle(n):
    """function create triangle pascal"""

    lists = []
    for x in range(n):
        temp_list = []
        num1 = -1
        num2 = 0
        for m in range(x + 1):
            if m == 0 or m == x:
                temp_list.append(1)
            else:
                temp_list.append(aux[num1] + aux[num2])
            num1 += 1
            num2 += 1
        lists.append(temp_list)
        aux = temp_list[:]
    return lists

