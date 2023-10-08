#!/usr/bin/python3

"""
    Start of the program
"""


from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """
        Main Function, adds all arguments to a Python list, and then saves
        them to a file
    """

    fileName = "add_item.json"
    try:
        with open(fileName, "r") as f:
            if f.read() == "":
                save([], fileName)
    except Exception:
        save([], fileName)

    cont = load(fileName)

    for i in range(1, len(argv)):
        cont.append(argv[i])

    save(cont, fileName)
