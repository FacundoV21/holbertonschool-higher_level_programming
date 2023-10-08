#!/usr/bin/python3
"""
    Start of the program
"""
from sys import argv
from os.path import exists
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if exists("add_item.json"):
    cont = load("add_item.json")
else:
    cont = []

for i in range(1, len(argv)):
    cont.append(argv[i])
save(cont, "add_item.json")
