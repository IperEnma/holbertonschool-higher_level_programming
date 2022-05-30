#!/usr/bin/python3
"""modulo with function that returns the list of available attributes"""


def lookup(obj):
    """returns the list of available attributes and methods"""

    return (dir(obj))
