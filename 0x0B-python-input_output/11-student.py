#!/usr/bin/python3
"""module with class"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initialize class"""
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
        my_dest = self.__dict__
        dict_dest = {}
        for key, value in my_dest.items():
            for attr in attrs:
                if key == attr:
                    dict_dest.update({key: value})

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            for key_, value_ in self.__dict__.items():
                if key == key_:
                    self.__dict__.update({key: value})
