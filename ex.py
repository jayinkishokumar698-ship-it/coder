def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def main(operation, x, y):
    print("simple calculator")
    print("Available operations: +, -, *, /")

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")


        if operation == '+':
            result = add(x, y)
        elif operation == '-':
            result = subtract(x, y)
        elif operation == '*':
            result = multiply(x, y)
        elif operation == '/':
            result = divide(x, y)
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
            return

        print(f"The result of {x} {operation} {y} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main(None, None, None)