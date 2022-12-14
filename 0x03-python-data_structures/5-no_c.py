#!/usr/bin/python3


def no_c(my_string):
    if my_string is not None:
        new_string = my_string.translate({ord(c):None for c in "cC"})
        return (new_string)
