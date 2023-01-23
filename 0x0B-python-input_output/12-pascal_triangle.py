#!/usr/bin/python3
"""
returns a list of integers
representing pascal triangle on n
"""


def pascal_triangle(n):
    """
    parameters:
    @n - number of rows
    Returns -list of integers
    """
    res = []
    row_list = []

    if n <= 0:
        return []

    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(row_list[y] + row_list[y - 1])
        row_list = row
        res.append(row)
    return res
