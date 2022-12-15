#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list is not []:
        new_list = []
        for i in range(0, len(my_list)):
            if i % 2 == 0:
                new_list.append([i])
            else:
                new_list.append(0)
        return (new_list)
    else:
        new_list = my_list
        return (new_list)
