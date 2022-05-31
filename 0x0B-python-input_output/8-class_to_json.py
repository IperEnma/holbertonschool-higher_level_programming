#!/usr/bin/python3
"""module with class"""

import json


def class_to_json(obj):
    """class to json list, dictionary, string, int, bool"""

    return (obj.__dict__)
