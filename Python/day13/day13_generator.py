# Generator - are memory efficient because they generate values on the fly instead of storing in memory 
def abc():
    yield 1  #yield keyword makes a def/func to convert it into generator
    yield 2
    yield 3

for value in abc():
    print(value)




def count(n):
    c = 1   #reference value
    while c<=n:
        yield c
        c+=1

for num in count(4):
    print(num)