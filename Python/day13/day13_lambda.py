from functools import reduce 
# x = lambda a:a+10
# print(x(5))

# y = lambda a,b:a*b
# print(x(2,3))

# z = lambda a,b,c : a+b+c
# print(z(1,2,3))

a = [1,2,3,4,5]
b = map(lambda x:x**2, a)
print(list(b))

c = reduce(lambda f,g:f+g, a)
print(c)
#import reduce
#define lambda : must accept 2 arguements
#call reduce