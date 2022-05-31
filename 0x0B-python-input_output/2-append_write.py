#!/usr/bin/python3
"""module append text file"""


def append_write(filename="", text=""):
    """function append text file"""

    with open(filename, 'a') as f:
        characters = f.write(text)
    return characters
