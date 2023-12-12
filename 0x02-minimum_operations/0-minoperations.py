#!/usr/bin/python3
"""
Calculates the fewest number of operations needed
to result in exactly n H characters in a file.
"""


def minOperations(n):
    """ Description: Takes in a given number n and calculates
                     the minimum operations needed. """
    if n <= 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
