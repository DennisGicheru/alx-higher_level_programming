#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        pass
    finally:
        if b != 0:
            print("Inside Result: {}".format(c))            
        else:
            print("Inside Result: None")
            return(None)
    return(c)
