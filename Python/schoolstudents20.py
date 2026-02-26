students={}

for i in range(1,21):
    surname=input("Enter surname: ")
    name=input("Enter name: ")

    students[surname]=name

for surname,name in students.items():
    print({surname},{name})