# list comprehension - a way to create new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if condition]
# list = [expression if/else for item in iterable] 
'''
# using normal loop method
marks = [70,48,80,79,93,32,42,64,59,96]
pass_students = []
fail_students = []

for i in marks:
    if i >= 60:
        pass_students.append(i)
    else:
        fail_students.append(i)
print(pass_students)
print(fail_students)
'''


#Using list comprehension method
marks = [70,48,80,79,93,32,42,64,59,96]

# pass_studentes = list(filter(lambda x:x>=60, marks))   # using lambda and filter also we can create a new list from the existing list based on a condition
# print(pass_studentes)
pass_marks = [i if i >= 60 else "failed" for i in marks]
print(pass_marks)

fail_marks = [i if i < 60 else 'passed' for i in marks]
print(fail_marks)