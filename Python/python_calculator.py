def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select Operation: +, -, *, /")
op = input("Enter operator: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", add(num1, num2))
elif op == "-":
    print("Result:", subtract(num1, num2))
elif op == "*":
    print("Result:", multiply(num1, num2))
elif op == "/":
    if num2 != 0:
        print("Result:", divide(num1, num2))
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operator!")
