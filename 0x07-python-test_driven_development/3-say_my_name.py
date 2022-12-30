#!/usr/bin/python3
"""
Simple function that prints two names
order: first name, second name
"""


def say_my_name(first_name, last_name=""):
    """
    simple function to print two names
    Args:
        first_name(str): <first name>
        last_name(str): < last name>
    Raise:
        TypeError
        if either first name or last_name is not str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
