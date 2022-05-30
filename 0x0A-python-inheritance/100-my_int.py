#!/usr/bin/python3
"""module subclass int"""


class MyInt(int):
    """define class"""

    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
