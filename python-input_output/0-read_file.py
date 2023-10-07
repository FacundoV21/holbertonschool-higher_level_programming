#!/usr/bin/python3
"""
    Start of the program
"""


def read_file(filename=""):
    """
        Function to read form a file
    """
    with open(filename, encoding="utf-8") as f:
        read = f.read()
    print(read, end="")
