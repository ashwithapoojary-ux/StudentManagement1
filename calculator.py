# Define functions for each arithmetic operation
def add(x, y):
    """Returns the sum of two numbers"""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers"""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers"""
    return x * y

def divide(x, y):
    """Returns the quotient of two numbers, handling division by zero"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

# --- Example Usage ---

# 1. Ask the user for input
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # 2. Call the functions and display results
    print(f"\nResults for {num1} and {num2}:")
    print(f"Addition:       {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction:    {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    print(f"Division:       {num1} / {num2} = {divide(num1, num2)}")

except ValueError:
    print("Invalid input! Please enter numbers only.")
