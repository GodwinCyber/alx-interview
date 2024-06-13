#!/usr/bin/python3
"""calculate the minimum number"""


def minOperations(n):
    """If n is less than 2, return 0 because we
        cannot perform on a single character
        Initialize the number of operations to 0
        Start with smallest prime number
    """
    if n < 2:
        return 0
    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n
    return operations
