def get_a_valid_number():
    """
    This asks the user for a number.
    It wants a number that's not negative.
    """
    while True:
        try:
            input_from_user = input("Enter a non-negative integer: ")
            the_number = int(input_from_user)
            if the_number >= 0:
                return the_number
            else:
                print("That's negative! Try again.")
        except ValueError:
            print("That's not a number. Try again.")

def calculate_the_factorial(input_number):
    """
    This calculates the factorial.
    Multiplies all the numbers.
    """
    if input_number == 0:
        return 1
    else:
        result_of_calculation = 1
        for current_number in range(1, input_number + 1):
            result_of_calculation *= current_number
        return result_of_calculation

def run_the_program():
    """
    This is where everything starts.
    Gets the number, calculates, and prints.
    """
    number_to_use = get_a_valid_number()
    factorial_result = calculate_the_factorial(number_to_use)
    print(f"The factorial of {number_to_use} is: {factorial_result}")

if __name__ == "__main__":
    run_the_program()
