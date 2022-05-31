#!/usr/bin/python3
"""moodule from json string to object"""

import json


def from_json_string(my_str):
    """function from  json string to object"""

    obj = json.loads(my_str)
    return obj
