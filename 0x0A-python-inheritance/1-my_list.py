#!/usr/bin/pyhton3
"""class that inherits"""


class MyList(list):
    """class list"""

    def __init__(self):
        """initialize function"""
        super().__init__()

    def print_sorted(self):
        """function with class that inherits"""
        sorted_list = sorted(self)
        print(sorted_list)
