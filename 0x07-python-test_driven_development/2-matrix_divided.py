#!/usr/bin/python3
"""
Simple function that divides a matrix
by a div and returns all results to 
2 decimal places """


def matrix_divided(matrix, div):
    """
    Conditions
        1. Confirm matrix is of type int or float
        2. Each row of the matrix must be of same size
    if not Raise TypeError(s)
    """
    if type(matrix) is not list or not all((type(item) is list) for item in matrix) \
        or not all((isinstance(element, (int, float))for element in item)for item in matrix) \
        or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if (div is None or not isinstance(div, int) and (not isinstance(div, float))):
        raise TypeError("div must be a number")

    n = len(matrix[0])
    if not all((len(row) == n)for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda x: round(x / div, 2), row))for row in matrix])
