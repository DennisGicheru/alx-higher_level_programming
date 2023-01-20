#!/usr/bin/python3
import json

"""Returns the JSON representation
   of an object(string)"""


def to_json_string(my_obj):
    """use dumps method"""
    return (json.loads(my_obj))
