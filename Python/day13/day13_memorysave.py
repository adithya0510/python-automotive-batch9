def large_num(n):
    for i in range(n):
        yield i


#this doesnot create a lakh numbers in memory
gen = large_num(10)
print(next(gen))
print(next(gen))
print(next(gen))

#basic list comprehension - uses much memory for each element
list = [x*x for x in range(5)]
print(list)

#comprehension using generator - dont use much memory
gen=(x*x for x in range(5))
print(gen)
