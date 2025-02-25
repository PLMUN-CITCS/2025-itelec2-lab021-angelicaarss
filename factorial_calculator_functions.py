def get_user_number():
    """Gets a non-negative integer from the user."""
    while True:
        try:
            input_string = input("Enter a non-negative integer: ")
            user_number = int(input_string)
            if user_number >= 0:
                return user_number
            else:
                print("Negative number. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

def calculate_factorial(input_number):
    """Calculates the factorial of the input number."""
    factorial_result = 1
    if input_number == 0:
        return factorial_result
    else:
        for i in range(1, input_number + 1):
            factorial_result *= i
        return factorial_result

def run_program():
    """Runs the factorial calculation program."""
    number_to_calculate = get_user_number()
    final_result = calculate_factorial(number_to_calculate)
    print(f"The factorial of {number_to_calculate} is: {final_result}")

if __name__ == "__main__":
    run_program()
