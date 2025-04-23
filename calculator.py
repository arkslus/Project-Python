# This program does simple calculations
# Add two numbers
def add(a, b):
    return a + b

# Subtract two numbers
def subtract(a, b):
    return a - b

# Multiply two numbers
def multiply(a, b):
    return a * b

# Divide two numbers
def divide(a, b):
    return a / b

# create a dictionary to store the operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Initialize the variables
should_continue = True

# Loop until the user chooses to exit
while should_continue:
    # Get the operation from the user
    operation = input("Enter one of these operations for your calculation (+, -, *, /): ")

    # Get the two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Check if the operation is valid
    if operation in operations:
        # Get the function associated with the operation
        operation_func = operations[operation]

        # Perform the operation and print the result
        result = operation_func(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        # Ask the user if they want to continue
        should_continue = input(f"Do you want to perform another calculation with {result}? (yes/no): ").lower()
        if should_continue == "yes":
            num1 = result
        else:
            should_continue = False
            print("\n" * 20, "Goodbye!")
            # Reset the operation variable
            operation = None
