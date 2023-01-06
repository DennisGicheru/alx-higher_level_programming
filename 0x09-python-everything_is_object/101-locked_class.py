#!/usr/bin/python3
"""
class with no attribute or object
"""


class LockedClass:
    """
    will not create class until name is first_name
    """
    __slots__ = 'first_name'
