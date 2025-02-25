def get_number():
    """
    Get a non-negative integer from the user.
    
    Prompts the user to enter a non-negative integer and returns it.
    Ensures that the input is a valid non-negative integer.
    :return: A non-negative integer entered by the user.
    """
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                return num
            else:
                print("Negative numbers are not allowed.")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def factorial(n):
    """
    Calculate the factorial of a number.
    
    Computes the factorial of the given non-negative integer.
    :param n: A non-negative integer.
    :return: The factorial of the given integer.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    """
    Main function to calculate the factorial of a user-provided number.
    
    Calls get_number() to get a non-negative integer from the user.
    Calls factorial() to compute the factorial of the provided number.
    Prints the factorial of the provided number.
    """
    number = get_number()
    fact = factorial(number)
    print(f"The factorial of {number} is: {fact}")

if __name__ == "__main__":
    main()
