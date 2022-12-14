#!/usr/bin/pthon3


def multiple_returns(sentence):
    i = 0
    list_a = list(sentence)
    first = ""
    length = len(list_a)

    if len(list_a) != 0:
        first = list_a[0]
        for character in list_a:
            i += 1
    else:
        first = None

    tuple_new = tuple(list_a)
    return(i, first)
