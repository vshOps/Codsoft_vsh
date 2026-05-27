# Simple Calculator Program

# Take first number from user
num1 = float(input("Enter first number: "))

# Take second number from user
num2 = float(input("Enter second number: "))

# Ask user to choose operation
print("\nChoose Operation")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation = input("Enter operation: ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    print("Result =", result)

elif operation == "-":
    result = num1 - num2
    print("Result =", result)

elif operation == "*":
    result = num1 * num2
    print("Result =", result)

elif operation == "/":
    
    # Check division by zero
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operation")