#!/usr/bin/python3
"""Module - JSON representation of an object"""

import json


def to_json_string(my_obj):
    """function - JSONs representation of an object"""

    json_string = json.dumps(my_obj)
    return json_string
