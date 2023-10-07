#!/usr/bin/python3
"""
    Start of the program
"""


def write_file(filename="", text=""):
    """
        Function to write into a file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
    
    return num
