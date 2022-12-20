#!/usr/bin/python3


def safe_print_integer(value):
    try:
        val = int(value)
        if val is not None:
            print("{:d}".format(val), end="")
            print("")
        return True
    except TypeError:
        return False
    except ValueError:
        return False
