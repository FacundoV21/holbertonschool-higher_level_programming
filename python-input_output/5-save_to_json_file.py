#!/usr/bin/python3
"""
    Start of the program
"""


import json


def save_to_json_file(my_obj, filename):
    """
        Returns an object represented by a JSON string
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
