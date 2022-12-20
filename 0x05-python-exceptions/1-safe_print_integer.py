#!/usr/bin/python3


def safe_print_integer(value):
    val = 0
    try:
        val = int(value)
        if val / 1 == val:
            print("{:d}".format(val))
        return True
    except ValueError:
        return False
