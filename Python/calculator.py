def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"  # division by 0 is not possible
    return a / b


# give input to a and b
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

'''
calling the functions and printing the output
print("Addition:", add(a,b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))
'''

#calling the functions and printing the output
print(add(a,b))  
print(sub(a,b))
print(mul(a,b))
print(div(a,b))