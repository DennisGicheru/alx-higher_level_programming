#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print('', end='')
    else:
        my_list.reverse()
    n = len(my_list)
    for i in range(n):
        print("{:d}".format(my_list[i]))
