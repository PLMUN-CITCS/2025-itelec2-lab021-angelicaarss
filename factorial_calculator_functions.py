"""
A module that calculates factorials and handles user input.
"""

def get_non_negative_integer() -> int:
    """
    Prompt the user to input a non-negative integer and return it.
    """
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                return num
        except ValueError:
            pass
        print("Invalid input. Please enter a non-negative integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a given non-negative integer.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    """
    Main entry point for the program.
    """
    number = get_non_negative_integer()
    print(f"The factorial of {number} is: {calculate_factorial(number)}")
