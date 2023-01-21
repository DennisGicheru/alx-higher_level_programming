#!/usr/bin/python3
"""
Function that adds all arguments to a python list
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_to_json_file

open("add_item.json", "a")
try:
    var = load_from_json_file("add_item.json")
except ValueError:
    var = []
save_to_json_file(var + sys.argv[1:], "add_item.json")
