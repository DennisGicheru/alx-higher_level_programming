#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print('', end='')
    else:
        for i in range(len(my_list)):
            j = len(my_list) - i
            print("{:d}".format(j))
