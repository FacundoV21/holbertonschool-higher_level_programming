#!/usr/bin/python3

"""
    Start of the program
"""

from sys import argv
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """
        Main Function, adds all arguments to a Python list, and then saves
        them to a file
    """

    fileName = "add_item.json"
    try:
        with open(fileName, "r") as f:
            if f.read() == "":
                save_json([], fileName)
    except Exception:
        save_json([], fileName)

    cont = load_json(fileName)

    for i in range(1, len(argv)):
        cont.append(argv[i])

    save_json(cont, fileName)
