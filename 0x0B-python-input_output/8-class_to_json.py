#!/usr/bin/python3
"""
Returns dictionary description
with simple data structure
"""


def class_to_json(obj):
    """returns dictionary description
    with simple data structure (list,
    dictionary, string integer)
    """
    return(obj.__dict__)
