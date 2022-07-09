#!/usr/bin/python3
import math

def add_nums(a, b):
    """
    Takes two parameters
    returns the sum.
    """
    return a + b


def mul_nums(a, b):
    """
    Takes two parameters
    Returns the product
    """
    return a * b

print(add_nums(10, 25))
print(add_nums.__doc__)

print(mul_nums(10, 5))
print(mul_nums.__doc__)

print(math.__doc__)
