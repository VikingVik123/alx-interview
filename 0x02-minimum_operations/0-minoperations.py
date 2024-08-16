#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute two operations in this file: Copy All and Paste
Given a number n
write a method that calculates the fewest number of operations
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Function initialization
    """
    if n == 0:
        return 0

    operation = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operation += factor
            n //= factor
        factor += 1
    return operation