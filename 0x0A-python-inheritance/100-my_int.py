#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """
        a class MyInt that inherits from int
    """
    def __eq__(self, value):
        """eq"""
        return not super().__eq__(value)

    def __ne__(self, value):
        """not eq"""
        return not super().__ne__(value)
