#!/usr/bin/python3


def best_score(a_dictionary):
    n = 0
    if a_dictionary:
        for k in a_dictionary:
            if a_dictionary[k] > n:
                max_key = max(a_dictionary, key=a_dictionary.get)
                return(max_key)
            else:
                return None
