#!/usr/bin/python3
"""A function that returns a list of integers
representing pascal's triangle of n"""


def pascal_triangle(n):
    """
    returns a lists of integers
    representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    pascal_triangle = [[1]]
    while len(pascal_triangle) != n:
        previous = pascal_triangle[-1]
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        pascal_triangle.append(current)
    return pascal_triangle
