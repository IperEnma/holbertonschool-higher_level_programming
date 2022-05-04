#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dic = a_dictionary.copy()
    for key, val in dic.items():
        if val == value:
            a_dictionary.pop(key, None)
    return a_dictionary
