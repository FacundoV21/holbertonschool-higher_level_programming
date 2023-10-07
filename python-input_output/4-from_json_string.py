#!/usr/bin/python3
"""
    Start of the program
"""


import json


def from_json_string(my_str):
    """
        Returns an object represented by a JSON string
    """
    return json.loads(my_str)
