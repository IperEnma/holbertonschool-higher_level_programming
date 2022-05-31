#!/usr/bin/python3
"""module triangle pascal"""


def pascal_triangle(n):
    """function triangle pascal"""

    lists = []
    for x in range(n):
        temp_list = []
        num1 = -1
        num2 = 0
        temp_list = []
        for m in range(x + 1):
            if num1 == -1 or num2 == len(aux):
                temp_list.append(1)
            else:
                temp_list += [aux[num1] + aux[num2]]
            num1 += 1
            num2 += 1
        lists.append(temp_list)
        aux = temp_list[:]
    return lists
