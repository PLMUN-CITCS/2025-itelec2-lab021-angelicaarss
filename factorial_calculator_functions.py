"""
Module for factorial calculation functions.
"""

def factorial(n):
    """
    Calculate the factorial of a number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def greet():
    """
    Function to greet.
    """
    print("Hello, world")

# Ensure the file ends with a newline
