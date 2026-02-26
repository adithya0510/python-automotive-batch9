def log_function(func):
    def wrapper(args,**args2):
        print("Calling function:{func._name_}")
        result = func(*args,**args2)
        print("function name:{func._name_}")
        return result
    return wrapper    

@log_function
def greeting(name):
    return f"hello,{name}"