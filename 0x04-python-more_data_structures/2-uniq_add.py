#!/usr/bin/python3


def uniq_add(my_list=[]):
    result = 0
    set_a = set(my_list)

    for val in set_a:
        result += val
    return(result)
