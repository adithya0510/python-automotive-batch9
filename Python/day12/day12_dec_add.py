def calculator(func):
    def wrapper(a,b):
        addition = a + b
        print(f"Addition:{addition}")
        return addition
    return wrapper

@calculator
def add(a,b):
    pass
print("Addition using calculator decorator")
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
add(a,b)