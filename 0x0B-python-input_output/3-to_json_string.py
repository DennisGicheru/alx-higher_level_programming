#!/usr/bin/python3
"""
Returns the JSON representation
of an object(string)
"""
import json


def to_json_string(my_obj):
    """use loads method
    @my_obj -object to be loaded
    """
    return json.dumps(my_obj)
