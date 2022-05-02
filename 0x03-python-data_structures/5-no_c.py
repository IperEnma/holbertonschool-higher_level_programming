#!/usr/bin/python3
def no_c(my_string):
    result = ''
    for x in my_string:
        if x == 'c' or x == 'C':
            x = ''
        result = result + x
    return result
