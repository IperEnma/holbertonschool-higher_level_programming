#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        integer = my_list[0]
        for x in my_list:
            if x > integer:
                integer = x
        return integer
    else:
        return None
