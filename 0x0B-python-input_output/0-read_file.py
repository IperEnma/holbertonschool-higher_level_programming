#!/usr/bin/python3
"""module reads text file"""


def read_file(filename=""):
    """reads a text file (UTF8)"""

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
