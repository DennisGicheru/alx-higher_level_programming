#!/usr/bin/python3

"""
if object is instance of or if object is instance of a class
"""
def is_kind_of_class(obj, a_class):
    """Returns True if condition is met
        @args:
         obj(anything): object to the checked
    a_class(anything): to be checked
    """
    if isinstance(obj, a_class):
        """checks if instance of or isinstanceof class"""
        return True
    return False
