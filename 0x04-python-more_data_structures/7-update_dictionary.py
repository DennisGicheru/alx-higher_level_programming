#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    for item in a_dictionary:
        if item == key:
            a_dictionary[key] = value
    return (a_dictionary)
