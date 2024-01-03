#!/usr/bin/python3
"""
Validates if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    num_consecutive_ones = 0

    b1 = 1 << 7
    b2 = 1 << 6

    for byte in data:
        b = 1 << 7
        if num_consecutive_ones == 0:
            while b & byte:
                num_consecutive_ones += 1
                b = b >> 1
            if num_consecutive_ones == 0:
                continue
            if num_consecutive_ones == 1 or num_consecutive_ones > 4:
                return False
        else:
            if not (byte & b1 and not (byte & b2)):
                return False
        num_consecutive_ones -= 1
    return num_consecutive_ones == 0