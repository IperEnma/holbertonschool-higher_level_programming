#!/usr/bin/python3
"""module writes an Object to txt"""

import json


def save_to_json_file(my_obj, filename):
    """function writes an Object to txt"""

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
