import art

# -------------------- Math operation functions --------------------

def add(n1, n2):
    """Returns the sum of two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference of two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Returns the division of two numbers. Handles divide by zero by returning None."""
    if n2 == 0:
        print("Error: Cannot divide by zero")
        return None  # Returning None indicates an invalid operation
    return n1 / n2

def modulus(n1, n2):
    """Returns the modulus (remainder) of two numbers"""
    return n1 % n2

def power(n1, n2):
    """Returns the first number raised to the power of the second"""
    return n1 ** n2

# -------------------- Operation dictionary --------------------
# Maps operator symbols to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulus,
    "**": power,
}

# -------------------- Calculator logic --------------------
def calculator():
    """Main calculator function"""

    # Outer loop allows restarting the calculator with a new first number
    while True:
        print(art.logo)
        first_number = float(input("What is the first number?: "))

        # Inner loop allows continuous calculations using the previous result
        while True:
            print("+\n-\n*\n/\n%\n**")  # Show available operations
            symbol = input("Pick an operation: ")

            # Validate the operator
            if symbol not in operations:
                print("Invalid operation. Please choose again.")
                continue  # Skip the rest and ask for a valid operator

            # Ask for the next number
            next_number = float(input("What is the next number?: "))

            # Call the correct function from the dictionary
            result = operations[symbol](first_number, next_number)

            # Handle invalid operation (like division by zero)
            if result is None:
                continue  # Skip the rest and ask for a new operator

            # Display the result
            print(f"{first_number} {symbol} {next_number} = {result}")

            # Update first_number to the latest result to allow chaining calculations
            first_number = result

            # Ask the user how to continue
            choice = input(
                f"Type 'y' to continue calculating with {result}, "
                f"'n' to start a new calculation, "
                f"or 'q' to quit: "
            ).lower()

            # Continue with the current result
            if choice == "y":
                first_number = result  # Already updated above

            # Start a new calculation
            elif choice == "n":
                break  # Exit inner loop → back to outer loop for new first number

            # Exit the calculator completely
            else:
                print("Goodbye 👋")
                return  # Exit the function

# -------------------- Start the calculator --------------------
calculator()
