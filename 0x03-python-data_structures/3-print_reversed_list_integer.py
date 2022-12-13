#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    for i in range(n)):
        my_list[i] = my_list[n-i]
        return my_list
