#!/usr/bin/python3

"""Class Mylist that inherits from list"""


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """public instance method"""
        print("{}".format(sorted(self)))
