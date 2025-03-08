"""
A module for calculating factorials with improved input validation and clarity.
"""

def get_non_negative_integer() -> int:
    """
    Prompts the user to enter a non-negative integer and returns it.

    Handles invalid input by providing specific error messages.
    """
    while True:
        try:
            user_input = input("Enter a non-negative integer: ")
            number = int(user_input)
            if number < 0:
                print("Error: Please enter a non-negative integer.")
            else:
                return number
        except ValueError:
            if user_input.strip() == "":
                print("Error: Input cannot be empty. Please enter an integer.")
            else:
                print("Error: Invalid input. Please enter a valid integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.

    Args:
        n: The non-negative integer.

    Returns:
        The factorial of n.
    """
    if n == 0:
        return 1  # Factorial of 0 is 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    number = get_non_negative_integer()
    factorial_result = calculate_factorial(number)
    print(f"The factorial of {number} is: {factorial_result}")
