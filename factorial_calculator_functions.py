def get_a_good_number():
  """
  Yo, this thing gets a number from the user.
  It wants a number that's not negative.
  """
  while True:
    try:
      user_input = input("Enter a non-negative integer: ") # Matching prompt
      number = int(user_input)
      if number >= 0:
        return number
      else:
        print("Hey, that's negative! Try again.")
    except ValueError:
      print("That ain't a number, dude. Try again.")

def do_the_factorial_thing(n):
  """
  This bit does the factorial stuff.
  Like, multiplies all the numbers.
  """
  if n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result = result * i
    return result

def run_the_whole_show():
  """
  This is where it all goes down.
  Gets the number, does the factorial, tells the user.
  """
  the_number = get_a_good_number()
  factorial_result = do_the_factorial_thing(the_number)
  print("The factorial of", the_number, "is:", factorial_result) # Matching output

if __name__ == "__main__":
  run_the_whole_show()