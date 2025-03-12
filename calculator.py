def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

# Map operations to functions
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation in operations:
            result = operations[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Invalid operation")
    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    calculator()
