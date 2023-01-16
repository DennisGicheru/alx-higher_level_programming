#!/usr/bin/python3

"""function to check if instance is of specified class"""


def is_same_class(obj, a_class):
    """checks if instance is of the same class
        Args:
         obj(object): to be checked
         a_class(anything): to be checked
     """
    if type(obj) == a_class:
        return True
    return False
