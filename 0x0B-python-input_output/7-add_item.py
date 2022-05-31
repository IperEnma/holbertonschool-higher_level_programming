#!/usr/bin/python3
"""module add all arguments to a python list"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys

try:
    my_list = load_from_json_file("add_item.json")
except:
    my_list = []

for x in sys.argv[1:]:
    my_list.append(x)

save_to_json_file(my_list, "add_item.json")
