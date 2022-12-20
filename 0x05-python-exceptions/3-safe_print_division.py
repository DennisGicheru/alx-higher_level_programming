#!/usr/bin/python3


def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
        return None
    finally:
        print("Inside Result: {}".format(c))
    return(c)
