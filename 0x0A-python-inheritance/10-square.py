#!/usr/bin/python3
"""module create square"""

base = __import__("9-rectangle").Rectangle

class Square(base):
    """define class"""

    def __init__(self, size):
        """define class"""
        super().__init__(size, size)
