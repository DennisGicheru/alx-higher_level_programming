#!/usr/bin/python3
def print_last_digit(number):
    num_str = repr(number)

    last_digit_str = num_str[-1]

    last_digit = int(last_digit_str)

    print("{}".format(last_digit), end="")

    return(last_digit)
