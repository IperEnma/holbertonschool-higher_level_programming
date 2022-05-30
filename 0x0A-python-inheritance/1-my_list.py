#!/usr/bin/python3
"""class that inherits"""


class MyList(list):
    """class list"""

    def print_sorted(self):
        """function with class that inherits"""
        sorted_list = sorted(self)
        print(sorted_list)
