#!/usr/bin/python3
"""
    Module to declare list of available attributes and methods of an object
"""

class MyList(list):
    """
        MyList class
    """

    def print_sorted(self):
        """
            This function sorts and prints the list
        """
        list_copy = self[:]
        print(sorted(list_copy))