# tuple - collection which is ordered and unchangable, used to group together related data.

student = ('Bro',21, 21, 'male')
print(student.count("Bro"))  # counts the occurence of specified value
print(student.index('male'))
print(student.count(21))

for i in student:
    print(i)

if "Bro" in student:
    print("Bro is here!")