#!/usr/bin/python3
"""
Function that adds all arguments to a python list
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_to_json_file

with open("add_item.json", "a") as f:
    try:
        items = load_from_json_file(f)
    except ValueError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, f)
