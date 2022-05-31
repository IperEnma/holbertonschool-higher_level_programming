#!/usr/bin/python3
"""module writes a string to a text file"""


def write_file(filename="", text=""):
    """function writes a string to a text file"""

    with open(filename, 'w') as f:
        characters = f.write(text)
    return characters
