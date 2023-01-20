#!/usr/bin/python3
"""
writes an object to a text file \
using json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    open file then write \
    to it using dump (without the s)
    """
    with open(filename, "w") as f:
        """use json.dump then place \
        2 parameters
        @my_obj - object to be added
        @f - representation of filename
        """
        return json.dump(my_obj, f)
