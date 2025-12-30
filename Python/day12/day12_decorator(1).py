#decorator
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
#calling decorator
@changecase
#decorated
def myfunc():
    return "hi"

print(myfunc())