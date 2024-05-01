def add(x, y):
  """Adds two numbers and returns the sum."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers and returns the difference."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers and returns the product."""
  return x * y

def divide(x, y):
  """Divides two numbers and returns the quotient, handling division by zero."""
  if y == 0:
    return "Error: Cannot divide by zero."
  else:
    return x / y

while True:
  # Get user input for operation
  print("\nSelect operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  choice = input("Enter choice(1/2/3/4/5): ")

  # Get numbers from user
  if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
  
  # Perform operation based on user choice
  if choice == '1':
    result = add(num1, num2)
    print(num1, "+", num2, "=", result)
  elif choice == '2':
    result = subtract(num1, num2)
    print(num1, "-", num2, "=", result)
  elif choice == '3':
    result = multiply(num1, num2)
    print(num1, "*", num2, "=", result)
  elif choice == '4':
    result = divide(num1, num2)
    print(num1, "/", num2, "=", result)
  elif choice == '5':
    print("Exiting calculator...")
    break
  else:
    print("Invalid Input")

