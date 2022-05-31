#!/usr/bin/python3
"""module creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """function load_from_json_file(filename)"""

    with open(filename) as f:
        json_str = f.read()
    obj = json.loads(json_str)
    return obj
