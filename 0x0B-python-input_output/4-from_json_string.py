#!/usr/bin/python3
"""
Returns object represented by JSON string
"""
import json


def from_json_string(my_str):
    """
    use loads method
    @my_str - string representing json
    """
    return json.loads(my_str)
