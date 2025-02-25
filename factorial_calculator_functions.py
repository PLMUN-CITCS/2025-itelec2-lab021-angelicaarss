def get_number():
    """Get number."""
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                return num
            else:
                print("Negative.")
        except ValueError:
            print("Invalid.")

def factorial(n):
    """Factorial."""
    result = 1
    if n == 0:
        return result
    else:
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    """Main."""
    number = get_number()
    fact = factorial(number)
    print(f"The factorial of {number} is: {fact}")

if __name__ == "__main__":
    main()
