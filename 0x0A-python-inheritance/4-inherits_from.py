#!/usr/bin/python3

"""
only sub class of instance
"""


def inherits_from(obj, a_class):
    """returns true if object is
    an instance of a class that inherited
    directly or indirectly from the specified
    class"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
