#!/usr/bin/python3
"""module with function that prints a text"""


def text_indentation(text):
    """function that prints a text"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    if text[0] == ' ':
        flag = 1
    else:
        flag = 0

    for x in text:
        if flag == 1 and x == ' ':
            continue
        else:
            flag = 0
            if x == '.' or x == '?' or x == ':':
                print(x)
                print()
                flag = 1
            else:
                print(x, end="")
