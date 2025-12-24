# Queues
'''queue1 = []   # Even student IDs
queue2 = []   # Odd student IDs

print("Enter student IDs (any values):")

for i in range(10):
    student_id = int(input("Enter Student ID: "))

    if student_id % 2 == 0:
        queue1.append(student_id)   # Even ID
    else:
        queue2.append(student_id)   # Odd ID

print("Queue 1:",queue1)
print("Queue 2",queue2) '''

# Parent class
class StudentID:
    def __init__(self):
        self.queue1 = []   #list1 to store the output
        self.queue2 = []   #list2 to store the output

    def user_id(self):
        print("Enter student IDs:")  #takes input from user
        for i in range(10):
            student_id = int(input("Enter Student ID: "))
            self.process_id(student_id)


# Child class (Inheritance)
class Queue(StudentID):   #Queue inherits from StudentID class

    def process_id(self, student_id):
        if student_id % 2 == 0:
            self.queue1.append(student_id)
        else:
            self.queue2.append(student_id)

    def display(self):
        print("Queue 1:",self.queue1)
        print("Queue 2:", self.queue2)



# Object creation
student = Queue()
student.user_id()
student.display()

