#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """only sub class of"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
