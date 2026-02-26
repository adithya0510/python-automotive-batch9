def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunc():
    return "hi"

print(myfunc())