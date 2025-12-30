# This function receives the original function (calculate) as 'func'
def calculator(func):

    # Wrapper function intercepts and replaces the original function call
    def wrapper(a, b):

        # Ask the user to choose the arithmetic operation
        choice = input("Enter Operation (+, -, *, /): ")

        if choice == '+':
            result = func(a, b, '+')
        elif choice == '-':
            result = func(a, b, '-')
        elif choice == '*':
            result = func(a, b, '*')
        elif choice == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            result = func(a, b, '/')
        else:
            return "Enter valid operator"
        return result
    return wrapper

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# This function receives the operator from the decorator
@calculator
def calculate(a, b, choice):
    if choice == '+':
        return add(a, b)

    elif choice == '-':
        return sub(a, b)

    elif choice == '*':
        return mul(a, b)

    elif choice == '/':
        return div(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Call the decorated function and print the result
print("Result:", calculate(a, b))
