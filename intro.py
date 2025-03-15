# Define functions for basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Dictionary to map operators to functions
operations = { 
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide 
}

# Example usage
first_number = 8
second_number = 4
operator = "+"  # Change this to test other operations


if operator in operations:
    result = operations[operator](first_number, second_number)

     
    print(f"{first_number} {operator} {second_number} = {result}")
else:
    print("Invalid operator")