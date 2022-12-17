#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    #return ([[row[i] ** 2 for i in range(3)] for row in matrix]) - Also works
    return ([list(map(lambda x: x ** 2, i)) for i in matrix]) 

