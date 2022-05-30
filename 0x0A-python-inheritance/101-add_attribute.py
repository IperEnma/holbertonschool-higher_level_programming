#!/usr/bin/python3
"""function adds a new attribute"""


def add_attribute(obj, name, value):

    if hasattr(obj, '__dict__') == True:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
