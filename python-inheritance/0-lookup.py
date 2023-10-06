#!/usr/bin/python3
"""
    Module to declare list of available attributes and methods of an object
"""
def lookup(obj):
    """
        Returns the list
    """
    return dir(obj)
