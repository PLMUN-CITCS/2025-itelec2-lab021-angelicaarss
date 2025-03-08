"""
This module provides functions for calculating factorials.
"""

def factorial(n):
    """
    Calculate the factorial of a number.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def another_function():
    """
    Description of what this function does.

    Returns:
    Type: Description of the return value.
    """
    # function implementation
