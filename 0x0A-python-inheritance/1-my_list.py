#!/usr/bin/pyhton3
"""class that inherits"""


class MyList:
    """define class"""

    def __init__(self):
        """initialize class"""
        self.__lista = []

    def append(self, num):
        """add element"""
        self.__lista.append(num)

    def print_sorted(self):
        """function with class that inherits"""
        sorted_list = sorted(self.__lista)
        print(sorted_list)

    def __str__(self):
        return str(self.__lista)

"""class MyList(list):

    def __init__(self):
        super().__init__()"""
