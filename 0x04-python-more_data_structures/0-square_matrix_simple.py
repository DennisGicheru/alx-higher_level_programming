#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix == []:
        return matrix
    else:
        new_matrix = matrix
        return ([[row[i] ** 2 for i in range(3)] for row in new_matrix])
