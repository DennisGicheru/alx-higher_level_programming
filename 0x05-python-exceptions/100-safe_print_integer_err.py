#!/usr/bin/python3
import sys
"""
function that prints an integer
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    else:
        return True
    finally:
        pass
