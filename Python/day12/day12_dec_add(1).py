# This function takes another function as an argument
def calculator(func):

    # Wrapper function (inner function)
    # This function will replace the original 'add' function
    def wrapper(a, b):
        addition = a + b
        print(f"Addition: {addition}")
        return addition
    return wrapper


# Applying the decorator to the add function
@calculator
def add(a, b):
    # Original function body is empty
    pass


print("Addition using calculator decorator")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Call the decorated function (actually calls wrapper)
add(a, b)
