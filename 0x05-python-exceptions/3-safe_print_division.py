#!/usr/bin/python3
"""
 divides 2 integers and prints the result.
     """


def safe_print_division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    else:
        return(c)
    finally:
        print("Inside result: {}".format(c))
