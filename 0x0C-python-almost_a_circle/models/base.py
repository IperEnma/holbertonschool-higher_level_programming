#!/usr/bin/python3
"""module with class base"""

import json


class Base:
    """define class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        my_list = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(my_list))
        else:
            for obj in list_objs:
                my_list.append(cls.to_dictionary(obj))
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        if (new):
            new.update(**dictionary)
        return(new)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        my_dict = {}
        my_list = []
        try:
            with open(cls.__name__ + ".json", "r") as f:
                my_dict = json.load(f)
        except Exception:
            return my_list
        for dict_ in my_dict:
            my_list.append(cls.create(**dict_))
        return my_list
