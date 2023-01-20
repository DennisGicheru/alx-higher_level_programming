#!/usr/bin/python3
"""
Creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    open file then create object \
    using load command (minus s)
    """
    with open(filename, "w") as f:
        """create object using
        f as representation of json
        file"""
        return json.load(f)
