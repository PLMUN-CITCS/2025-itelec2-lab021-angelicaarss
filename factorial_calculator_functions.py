def get_non_negative_integer():
    """
    Obtains a non-negative integer input from the user.

    Prompts the user to enter a non-negative integer and ensures the input is valid.
    Returns the validated non-negative integer.
    """
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number >= 0:
                return number
            else:
                print("Negative numbers are not allowed.")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def calculate_factorial(n):
    """
    Calculates the factorial of a given non-negative integer.

    :param n: A non-negative integer.
    :return: The factorial of the given integer.
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    """
    Main function to calculate the factorial of a user-provided number.

    Calls get_non_negative_integer() to get a valid input number.
    Calls calculate_factorial() to compute the factorial of the provided number.
    Prints the factorial of the provided number.
    """
    number = get_non_negative_integer()
    factorial_result = calculate_factorial(number)
    print(f"The factorial of {number} is: {factorial_result}")

if __name__ == "__main__":
    main()
