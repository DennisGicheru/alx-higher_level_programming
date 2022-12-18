#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    list_3 = []
    for i in list_1:
        if i not in list_2:
            list_3.append(i)
    for j in list_2:
        if j not in list_1:
            list_3.append(j)
    return (list_3)
