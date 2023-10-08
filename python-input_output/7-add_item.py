#!/usr/bin/python3
"""
    Start of the program
"""
from sys import argv
from os.path import exists
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if exists("add_item.json"):
    contenido = load_from_json_file("add_item.json")
else:
    contenido = []

for i in range(1, len(argv)):
    contenido.append(argv[i])

save_to_json_file(contenido, "add_item.json")
