#!/usr/bin/python3

"""
    Start of the program
"""


from sys import argv
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


fileName = "add_item.json"
cont = load(fileName)

with open(fileName, "w", encoding="utf-8") as f:
    for i in range(1, len(argv)):
        cont.append(argv[i])
    save(cont, fileName)
