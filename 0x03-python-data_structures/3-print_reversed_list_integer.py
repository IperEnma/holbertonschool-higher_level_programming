#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list):
        size = len(my_list)
        count = size - 1
        for x in range(-1, (size - 1)):
            print(my_list[count])
            count = count - 1
    return None
