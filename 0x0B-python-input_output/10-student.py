#!/usr/bin/python3
"""module with class student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        if type(attrs) is not list:
            return self.__dict__
        for x in attrs:
            if type(x) is not str:
                return self.__dict__
        else:
            dict_dest = {}
            my_dict = self.__dict__
            for key, value in my_dict.items():
                for x in attrs:
                    if x == key:
                        dict_dest.update({key: value})
            return (dict_dest)
